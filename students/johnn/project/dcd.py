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

# 
parser = optparse.OptionParser()
parser.add_option("-a", "--admin_port", dest="admin_port", help="Port of the admin interface on localhost")
parser.add_option("-p", "--pub_port", dest="pub_port", help="Port of the publisher interface on localhost")
parser.add_option("-d", "--debug", dest="debug", action="store_true", help="Print debug information to the screen")

(options, args) = parser.parse_args()

# hack to figure out my ip address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
myaddr = s.getsockname()[0]
s.close()

if options.admin_port is None:
    options.admin_port = "5561"

if options.pub_port is None:
    options.pub_port = "5556"

options.admin_interface = "tcp://{}:{}".format(myaddr,options.admin_port)
options.pub_interface = "tcp://{}:{}".format(myaddr,options.pub_port)
myinterfaces = ( options.admin_interface, options.pub_interface )

if options.debug is None:
    options.stream_log_level = logging.INFO
else:
    options.stream_log_level = logging.DEBUG

# look up process name, pid
scriptname = os.path.basename(__file__).split(".py")[0]
pid = os.getpid()

# define where to write the logs
log_path = 'log/{}-{}.log'.format(scriptname, pid)

# define a stream and file handler
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s:%(threadName)s %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setLevel(options.stream_log_level)
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler(filename = log_path)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

log.addHandler(file_handler)
log.addHandler(stream_handler)

# write out startup info to the log
log.info("process {}, PID {} starting".format(scriptname, pid))
log.info("logging to {}".format(log_path))
log.debug("screen log level {}".format(options.stream_log_level))

def decode_command(message):
    try:
        command, key, value = eval(message)
    except SyntaxError:
        command, key, value = (None, None, None)
    return ( command, key, value )

def blob(config):
    return repr( (myinterfaces, config.data, config.peers) )

def admin(config):
    context = zmq.Context()
    admin = context.socket(zmq.REP)
    admin.bind(options.admin_interface)
    log.info("admin bound on {}".format(options.admin_interface))

    talkback = context.socket(zmq.REQ)

    while True:
        command, key, value = decode_command(admin.recv_string())
        response = ""
        log.info("received command {}, key {}, value {}".format(command, key, value))
        if command == "dump":
            log.debug("dump request, responding {}".format(blob(config)))
            log.info("dump request")
            response = blob(config)
            admin.send_string(response)
        if command == "put":
            log.info("putting {} {}".format(key, value))
            config.pub_queue.put((key, value))
            config.sub_queue.put(key)
            response = "ack"
            admin.send_string(response)
        if command == "register":
            response = "registering {} {}".format(key, value)
            log.info(response)
            admin.send_string(reponse)
            config.peers[key]=value
        if command == "get":
            log.info("getting {}".format(key))
            try:
                config.sub_queue.put(key)
                value = config.get_value(key)
                response = value
                admin.send_string(response)
            except KeyError:
                config.sub_queue.put(key)
                response = ""
                admin.send_string(response)
        if command == "link":
            response = "initiating a link request to remote admin port at {}".format(value)
            log.debug(response)
            admin.send_string(response)
            log.debug("opening connection to " + str(value))
            talkback.connect(value)
            cmd = ("('dump', None, None)")
            log.debug("sending command " + cmd )
            talkback.send_string(cmd)  
            message = talkback.recv_string()
            log.debug("got " + str(message) )
            remote_ports, data, peers = eval(message)
            remote_admin, remote_pub = remote_ports
            config.peers[remote_admin] = remote_pub
            log.debug("remote_admin {}, remote_pub {}, data {}, peers {}".format(remote_admin, remote_pub, data, peers))
            for topic in data:
                log.debug("subscribing to topic {}".format(topic))
                config.sub_queue.put(topic)
                talkback.send_string("('get', '{}', None)".format(topic))
                message = talkback.recv_string()
                log.debug("queried key/value {}, got value {} from remote server".format(topic, message))
                config.pub_queue.put((topic, message))
            log.debug("asking {} to register my addresses".format(value))
            cmd = "('register', '{}', '{}')".format(options.admin_interface, options.pub_interface)
            log.debug("sending: " + cmd)
            talkback.send_string(cmd)
            message = talkback.recv_string()
            # disabled since this will cause an infinite loop
            # log.debug("asking {} to connect back to me ({})".format(value, options.admin_interface))
            # talkback.send_string("('link', None, '{}')".format(options.admin_interface))
            # message = talkback.recv_string()
            log.debug("got {}".format(message))


def pub(config):
    context = zmq.Context()
    pub = context.socket(zmq.PUB)
    pub.bind(options.pub_interface)
    log.info("pub bound on " + str(options.pub_interface))

    while True:
        try:
            key, value = config.pub_queue.get()
            config.set_value(key, value)
            pub.send_string("{} {}".format(key, value))
            log.info("published queue_entry {} {}".format(key, value))
        except queue.Empty:
            continue


def sub(config):
    # Socket to talk to server
    context = zmq.Context()
    socket = context.socket(zmq.SUB)

    log.info("sub thread working")

    while True:
        try:
            key = config.sub_queue.get()
            log.info("noticed sub queue_entry {}".format(key))
            socket.setsockopt_string(zmq.SUBSCRIBE, key)
        except queue.Empty:
            continue
        try:
            value = config.link_queue.get()
            log.info("noticed link queue_entry {}".format(value))
            socket.connect(value)
        except queue.Empty:
            continue
        string = socket.recv_string()
        key, value = string.split(" ", 1)
        config.set_value( key, value )
        log.info("sub got {} {}".format(key, value))


class Config():
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

config = Config()

admin_thread = Thread(target=admin, args=(config,))
pub_thread = Thread(target=pub, args=(config,))
sub_thread = Thread(target=sub, args=(config,))

log.debug("admin_thread is {}".format(admin_thread.name))
log.debug("pub_thread is {}".format(pub_thread.name))
log.debug("sub_thread is {}".format(sub_thread.name))

admin_thread.start()
pub_thread.start()
sub_thread.start()

