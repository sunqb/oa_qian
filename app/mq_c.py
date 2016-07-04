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

def consumer_msg(client):
    topic = client.topics['oa_qian']
    consumer = topic.get_simple_consumer()
    for message in consumer:
        if message is not None:
            print message.offset, message.value

if __name__ == '__main__':
    client = connectServer('kafka.sunqb.com:9092')
    consumer_msg(client)