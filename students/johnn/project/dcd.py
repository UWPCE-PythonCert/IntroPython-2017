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

# 
parser = optparse.OptionParser()
parser.add_option("-a", "--admin_port", dest="admin_port", help="Port of the admin interface on localhost")
parser.add_option("-p", "--pub_port", dest="pub_port", help="Port of the publisher interface on localhost")
parser.add_option("-d", "--debug", dest="debug", action="store_true", help="Print debug information to the screen")

(options, args) = parser.parse_args()

if options.admin_port is None:
    options.admin_port = "5561"

if options.pub_port is None:
    options.pub_port = "5556"

options.admin_interface = "tcp://*:{}".format(options.admin_port)
options.pub_interface = "tcp://*:{}".format(options.pub_port)

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

def admin(config):
    context = zmq.Context()
    admin = context.socket(zmq.REP)
    admin.bind(options.admin_interface)
    log.info("admin bound on {}".format(options.admin_interface))
    while True:
        #log.debug("admin listening")
        #message = admin.recv_string()
        command, key, value = decode_command(admin.recv_string())
        log.info("received command {}, key {}, value {}".format(command, key, value))
        admin.send_string("ack")
        if command == "dump":
            log.info("DUMP: " + str(config.data))
        if command == "put":
            log.info("putting {} {}".format(key, value))
            config.pub_queue.put((key, value))
        if command == "get":
            log.info("getting {}".format(key))
            config.sub_queue.put(key)
        if command == "link":
            log.info("linking {}".format(value))
            config.link_queue.put(value)


def pub(config):
    context = zmq.Context()
    pub = context.socket(zmq.PUB)
    pub.bind(options.pub_interface)
    log.info("pub bound on " + str(options.pub_interface))

    while True:
        try:
            key, value = config.pub_queue.get()
            pub.send_string("{} {}".format(key, value))
            config.set_value(key, value)
            log.info("published queue_entry {} {}".format(key, value))
        except queue.Empty:
            continue
        # topic = str(random.randrange(9999, 10005))
        # messagedata = (options.pub_port, random.randrange(1, 215) - 80)
        # log.debug("{} {}".format(topic, messagedata))
        # pub.send_string("{} {}".format(topic, messagedata))
        # time.sleep(2)

def sub(config):
    # Socket to talk to server
    context = zmq.Context()
    socket = context.socket(zmq.SUB)

    # listen to the following servers
    #socket.connect("tcp://localhost:%s" % 5556)
    #socket.connect("tcp://localhost:%s" % 5557)

    # subscribe to the following message types
    #socket.setsockopt_string(zmq.SUBSCRIBE, "10001")
    #socket.setsockopt_string(zmq.SUBSCRIBE, "9999")

    while True:
        try:
            queue_entry = config.sub_queue.get()
            log.info("noticed sub queue_entry {}".format(queue_entry))
            socket.setsockopt_string(zmq.SUBSCRIBE, queue_entry)
        except queue.Empty:
            continue
        try:
            queue_entry = config.link_queue.get()
            log.info("noticed link queue_entry {}".format(queue_entry))
            socket.connect(queue_entry)
        except queue.Empty:
            continue
        string = socket.recv_string()
        topic, message = string.split(" ", 1)
        config.set_value( topic, message )
        log.info("sub got {} {}".format(topic, message))

class Config():
    def __init__(self):
        self.pub_queue = queue.Queue()
        self.sub_queue = queue.Queue()
        self.link_queue = queue.Queue()
        self.data = {}
    def set_value(self, key, value):
        self.data[key] = value
    def get_value(self, key):
        return self.data[key]

config = Config()


pub_thread = Thread(target=pub, args=(config,))
admin_thread = Thread(target=admin, args=(config,))
#sub_thread = Thread(target=sub, args=(config,))

log.debug("pub_thread is {}".format(pub_thread.name))
log.debug("admin_thread is {}".format(admin_thread.name))

pub_thread.start()
admin_thread.start()

