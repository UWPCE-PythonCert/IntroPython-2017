#!/usr/bin/env python3

"""
Distributed Config Daemon (DCD)
"""

import zmq
import random
import sys
import os
import time
from threading import Thread
import logging
import optparse
import queue
import socket


class Config():
    """
    create a common config object to hold common state
    """
    def __init__(self):
        self.pub_queue = queue.Queue()
        self.sub_queue = queue.Queue()
        self.link_queue = queue.Queue()
        self.data = {}
        self.peers = {}
    def set_value(self, key, value):
        self.data[key] = value
    def get_value(self, key):
        return self.data[key]

    @property
    def myinterfaces(self):
        return ( self.admin_interface, self.pub_interface )

    @property
    def admin_interface_all(self):
        return "tcp://{}:{}".format("*",self.admin_port)

    @property
    def pub_interface_all(self):
        return "tcp://{}:{}".format("*",self.pub_port)

    @property
    def admin_interface(self):
        return "tcp://{}:{}".format(self.myaddr,self.admin_port)

    @property
    def pub_interface(self):
        return "tcp://{}:{}".format(self.myaddr,self.pub_port)


def process_arguments(config):
    """
    get the command line options and save them in the config object
    """

    parser = optparse.OptionParser()

    # allow overrides for ports and log level
    parser.add_option("-a", "--admin_port", dest="admin_port", default="5561", help="Port of the admin interface on localhost")
    parser.add_option("-p", "--pub_port", dest="pub_port", default="5556", help="Port of the publisher interface on localhost")
    parser.add_option("-d", "--debug", dest="debug", action="store_true", help="Print debug information to the screen")

    (options, args) = parser.parse_args()

    # hack to figure out my outgoing ip address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    config.myaddr = s.getsockname()[0]
    s.close()

    # look up process name, config.pid
    config.scriptname = os.path.basename(__file__).split(".py")[0]
    config.pid = os.getpid()

    # define the ports to use
    config.admin_port = options.admin_port
    config.pub_port = options.pub_port

    # bind to all ports
    # config.admin_interface_all = "tcp://{}:{}".format("*",options.admin_port)
    # config.pub_interface_all = "tcp://{}:{}".format("*",options.pub_port)
    # # port we want others to connect to
    # config.admin_interface = "tcp://{}:{}".format(config.myaddr,options.admin_port)
    # config.pub_interface = "tcp://{}:{}".format(config.myaddr,options.pub_port)
    # # 
    #config.myinterfaces = ( config.admin_interface, config.pub_interface )

    # choose logging level
    if options.debug is None:
        config.stream_log_level = logging.INFO
    else:
        config.stream_log_level = logging.DEBUG


def setup_logging(config):
    """
    set up logging

    set basic logging, always logging to a file at level debug,
    but logging to the screen at info or debug depending on the
    presence of the --debug flag
    """

    # define where to write the logs
    log_path = 'log/{}-{}.log'.format(config.scriptname, config.pid)

    # define a stream and file handler
    log = logging.getLogger()
    # always write debug to the log
    log.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s:%(threadName)s %(message)s')

    # set up console output
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(config.stream_log_level)
    stream_handler.setFormatter(formatter)

    # set up file output
    file_handler = logging.FileHandler(filename = log_path)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # start them up
    log.addHandler(file_handler)
    log.addHandler(stream_handler)

    # write out startup info to the log
    log.info("process {}, config.pid {} on {} starting".format(config.scriptname, config.pid, config.myaddr))
    log.info("logging to {}".format(log_path))
    log.debug("screen log level {}".format(config.stream_log_level))

    return log


def encode_message(command, key, value):
    """
    build a message string with the proper quoting
    """
    # we're building a string representation of a tuple,
    # with each value quoted, like "('get', 'dog', '')"
    return "({})".format(", ".join((repr(command), repr(key), repr(value))))


def decode_message(message):
    """
    decode a message or return None
    """
    try:
        command, key, value = eval(message)
    except SyntaxError:
        command, key, value = (None, None, None)
    return ( command, key, value )


def admin(config):
    """
    process the admin channel

    here we take commands sent to us over the admin interface and process them
    """
    context = zmq.Context()
    admin = context.socket(zmq.REP)
    log.debug("ADMIN INTERFACE " + config.admin_interface_all)
    admin.bind(config.admin_interface_all)
    log.info("admin bound on {}".format(config.admin_interface_all))

    while True:
        # get a message from the channel and decode it
        command, key, value = decode_message(admin.recv_string())
        # remember, we still have to respond to the admin channel
        log.debug("received command '{}', key '{}', value '{}'".format(command, key, value))

        if command == "dump":
            """
            example: (('tcp://192.168.1.209:5561', 'tcp://192.168.1.209:5556'),
              {'dog': 'black'}, {'tcp://192.168.1.34:5561': 'tcp://192.168.1.34:5556'})
            """
            response = encode_message(config.myinterfaces, config.data, config.peers)
            log.debug("responding to dump request with {}".format(response))
            admin.send_string(response)
            continue

        if command == "put":
            #log.info("performing a put of {}/{}".format(key, value))
            config.pub_queue.put((key, value))
            config.sub_queue.put(key)
            response = "{}/{} has been published".format(key, value)
            admin.send_string(response)
            continue

        if command == "register":
            config.peers[key]=value
            response = "{}/{} has been registered".format(key, value)
            log.info(response)
            admin.send_string(response)
            continue

        if command == "sync":
            """
            command = sync, key = None, value = <server to sync to>
            """
            # response = "ack sync to {}".format(value)
            # log.debug(response)
            # admin.send_string(response)
            # log.debug("opening connection to " + str(value))
            # s2s_admin.connect(value)
            # command = ("('dump', '', '')")
            # log.debug("sending command " + command )
            # s2s_admin.send_string(command)
            # message = s2s_admin.recv_string()
            # log.debug("got " + str(message) )
            # remote_ports, data, peers = eval(message)
            # # remote_admin, remote_pub = remote_ports
            # # config.peers[remote_admin] = remote_pub
            # # log.debug("remote_admin {}, remote_pub {}, data {}, peers {}".format(remote_admin, remote_pub, data, peers))
            # for topic in data:
            #     log.debug("subscribing to topic {}".format(topic))
            #     config.sub_queue.put(topic)
            #     s2s_admin.send_string("('get', '{}', '')".format(topic))
            #     message = s2s_admin.recv_string()
            #     log.debug("queried key/value {}, got value {} from remote server".format(topic, message))
            #     config.pub_queue.put((topic, message))
            # log.debug("asking {} to register my addresses".format(value))
            # command = "('register', '{}', '{}')".format(options.admin_interface, options.pub_interface)
            # log.debug("sending: " + command)
            # s2s_admin.send_string(command)
            # message = s2s_admin.recv_string()
            # # disabled since this will cause an infinite loop
            # # log.debug("asking {} to connect back to me ({})".format(value, options.admin_interface))
            # # s2s_admin.send_string("('link', None, '{}')".format(options.admin_interface))
            # # message = s2s_admin.recv_string()
            # log.debug("got {}".format(message))
            log.debug("sync disabled for now")
            continue

        if command == "get":
            """
            command = get, key = <key to get>, value = None
            """
            response = get_value(config, key)
            admin.send_string(response)
            continue

        if command == "link":
            """
            command = link, key = None, value = <admin port of remote server to link to>
            """
            response = "initiating a link request to remote admin port at {}".format(value)
            log.debug(response)
            message = s2s_admin("dump", '', '', value)
            remote_server_entries, data, peers = decode_message(message)
            remote_admin, remote_pub = remote_server_entries
            log.debug("saving remote server {} in database".format(remote_server_entries))
            config.peers[remote_admin] = remote_pub
            #log.debug("remote_admin {}, remote_pub {}, data {}, peers {}".format(remote_admin, remote_pub, data, peers))
            for topic in data:
                #log.debug("subscribing to topic {}".format(topic))
                config.sub_queue.put(topic)
                #response = get_value(config, topic)
                #admin.send_string(response)
                #s2s_admin.send_string("('get', '{}', None)".format(topic))
                #message = s2s_admin.recv_string()
                #log.debug("queried key/value {}, got value {} from remote server".format(topic, message))
                #config.pub_queue.put((topic, message))
            #log.debug("asking {} to register my addresses".format(value))
            message = s2s_admin("register", config.admin_interface, config.pub_interface, value)
            admin.send_string("got {}".format(message))
            continue

        command = ""


def get_value(config, key):
        """
        given a key, get a value

        command = get, key = <key to get>, value = None

        check locally first, then query the remote servers.
        return value or null
        """
        value = ""
        try:
            # try getting the value locally
            value = config.get_value(key)
            log.info("get_value fetched value {}/{} locally".format(key, value))
        except KeyError:
            if config.peers:
                log.debug("value not in local database, checking remote servers")
                for server in config.peers:
                    server_result = s2s_admin("get", key, "", server)
                    #log.debug("querying server {} for {}".format(server, key))
                    if server_result:
                        value = server_result
                        log.info("got value {}/{} from server {}".format(key, value, server))
                        # if we didn't find the value locally, but found it remotely, cache it
                        # in our local database
                        config.set_value(key, value)
                        log.debug("saved {}/{} to local database".format(key, value))
                        # subscribe to key to automatically get future updates
                        config.sub_queue.put(key)
                        log.debug("added {} to subcribe queue".format(key))
                        # stop as soon as we get a match
                        log.debug("terminating server search")
                        break
            else:
                log.debug("no remote servers, no matching entry")
        return value


def s2s_admin(command, key, value, remote_server):
    """
    send a command to remote server, return result
    """
    log.debug("s2s_admin called with cmd '{}', key '{}', value '{}', server '{}'".
        format(command, key, value, remote_server))
    context = zmq.Context()
    s2s_admin = context.socket(zmq.REQ)
    message = ""
    log.debug("opening s2s_admin connection to " + str(remote_server))
    s2s_admin.connect(remote_server)
    command = "({})".format(", ".join((repr(command), repr(key), repr(value))))
    log.info("sending s2s_admin command " + command)
    s2s_admin.send_string(command)
    message = s2s_admin.recv_string()
    log.info("received '" + str(message) + "' from remote server" )
    s2s_admin.disconnect(remote_server)
    log.debug("disconnected s2s_admin connection to " + str(remote_server))
    return message


def pub(config):
    """
    publish values found on the pub_queue
    """
    context = zmq.Context()
    pub = context.socket(zmq.PUB)
    pub.bind(config.pub_interface_all)
    log.info("pub thread bound on " + str(config.pub_interface_all))

    while True:
        try:

            # make sure we are connected to all remote servers
            for server in config.peers:
                pub_host = config.peers[server]
                log.debug("pub_subscriber connecting to {}".format(pub_host))
                pub.connect(pub_host)

            key, value = config.pub_queue.get()
            config.set_value(key, value)
            pub.send_string("{} {}".format(key, value))
            log.info("published pub_queue entry {}/{}".format(key, value))
        except queue.Empty:
            continue


def sub_subscriber(config):
    """
    subscribe to values found on the sub_queue
    """
    context = zmq.Context()
    sub = context.socket(zmq.SUB)
    sub.RCVTIMEO = 1000
    log.info("sub_subscriber thread working")

    while True:

        # make sure we are connected to all remote servers
        for server in config.peers:
            pub_host = config.peers[server]
            log.debug("sub_subscriber connecting to {}".format(pub_host))
            sub.connect(pub_host)

        try:
            # check the queue for an entry, subscribe to what you find
            key = config.sub_queue.get()
            sub.setsockopt_string(zmq.SUBSCRIBE, key)
            log.info("subscribed to sub_queue entry '{}'".format(key))

        except queue.Empty:
            # queue empty, nothing to do
            continue

        # check for subscriptions
        log.debug("checking for subscriptions")
        try:        
            subscription = sub.recv_string()
            key, value = subscription.split(" ", 1)
            # save value to the local database
            config.set_value( key, value )
            log.info("saved subscription {}/{} to local database".format(key, value))
        except Exception as err:
            log.debug("no subscrition activity, logged '{}'".format(err))


def sub_poller(config):
    """
    subscribe to values found on the sub_queue
    """
    # stub
    log.debug("sub_poller thread (barely) working")
    while True:
        time.sleep(5)
    # context = zmq.Context()
    # sub = context.socket(zmq.SUB)
    # log.info("sub_poller thread working")

    # while True:
    #     # try:
    #     #     # check the queue for an entry, subscribe to what you find
    #     #     key = config.sub_queue.get()
    #     #     sub.setsockopt_string(zmq.SUBSCRIBE, key)
    #     #     log.info("subscribed to sub_queue entry {}".format(key))

    #     # except queue.Empty:
    #     #     # queue empty, nothing to do
    #     #     continue

    #     # check for subscriptions
    #     subscription = sub.recv_string()
    #     key, value = subscription.split(" ", 1)
    #     # save value to the local database
    #     config.set_value( key, value )
    #     log.info("saved subsription {}/{} to local database".format(key, value))

        # try:
        #     value = config.link_queue.get()
        #     log.info("noticed link queue_entry {}".format(value))
        #     socket.connect(value)
        # except queue.Empty:
        #     continue


config = Config()

process_arguments(config)
log = setup_logging(config)

admin_thread = Thread(target=admin, args=(config,))
pub_thread = Thread(target=pub, args=(config,))
sub_subscriber_thread = Thread(target=sub_subscriber, args=(config,))
sub_poller_thread = Thread(target=sub_poller, args=(config,))

log.debug("admin_thread is {}".format(admin_thread.name))
log.debug("pub_thread is {}".format(pub_thread.name))
log.debug("sub_subscriber_thread is {}".format(sub_subscriber_thread.name))
log.debug("sub_poller_thread is {}".format(sub_poller_thread.name))

admin_thread.start()
pub_thread.start()
sub_subscriber_thread.start()
sub_poller_thread.start()
