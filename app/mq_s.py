#!/usr/bin/python
# -*- coding: UTF-8 -*-
#重新设置编码
import sys
import logging as log
from kafka import KafkaProducer
from kafka.errors import KafkaError


reload(sys)
sys.setdefaultencoding('utf8')

#log.basicConfig(level=log.DEBUG)

def producer_msg(serverlist):
    producer = KafkaProducer(bootstrap_servers=[serverlist])
    producer.send('oa_qian', b'async message')
    producer.flush()

if __name__ == '__main__':
    producer_msg('kafka.sunqb.com:9092')