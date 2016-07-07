#!/usr/bin/python
# -*- coding: UTF-8 -*-
#重新设置编码
import sys
import logging as log
import redis
import random

reload(sys)
sys.setdefaultencoding('utf8')

log.basicConfig(level=log.DEBUG)

class Task(object):

    def __init__(self):
        self.pubsub_channel = 'task:pubsub:channel';
        self.rcon = redis.StrictRedis(host='redis.sunqb.com', db=3)
        self.ps = self.rcon.pubsub()
        self.ps.subscribe(self.pubsub_channel)

    def listen_task(self):
        for i in self.ps.listen():
            print i;
            print i['data'];

    def pubsub(self):
        elem = random.randrange(10)
        print elem
        self.rcon.publish(self.pubsub_channel, elem)

if __name__ == '__main__':
    print 'listen task channel'
    Task().pubsub()
    #Task().listen_task()