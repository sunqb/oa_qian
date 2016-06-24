#!/usr/bin/python
# -*- coding: UTF-8 -*-
#重新设置编码
import sys
from pykafka import KafkaClient

reload(sys)
sys.setdefaultencoding('utf8')

def connectServer(hosts):
    client = KafkaClient(hosts)


if __name__ == '__main__':
    connectServer('kafka.sunqb.com:9092')