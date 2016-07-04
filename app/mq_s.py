#!/usr/bin/python
# -*- coding: UTF-8 -*-
#重新设置编码
import sys
import logging as log
from pykafka import KafkaClient

reload(sys)
sys.setdefaultencoding('utf8')

log.basicConfig(level=log.DEBUG)

def connectServer(hostlist):
    client = KafkaClient(hosts=hostlist)
    return client

def producer_msg(client):
    topic = client.topics['oa_qian']
    print topic
    producer = topic.get_producer()
    producer.produce('test message ')
    #for i in range(4):
    #    producer.produce('test message '+str(i ** 2))
    #producer.produce(['test message ' + str(i ** 2) for i in range(4)])

if __name__ == '__main__':
    client = connectServer('kafka.sunqb.com:9092')
    producer_msg(client)