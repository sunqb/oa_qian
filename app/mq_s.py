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
    #打印所有主题
    print client.topics


if __name__ == '__main__':
    connectServer('kafka.sunqb.com:9092')