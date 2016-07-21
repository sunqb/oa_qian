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
class Mq_s(object):

    def __init__(self, serverlist, msg):
        self.serverlist = serverlist;
        self.msg = msg

    def producer_msg(self):
        try:
            producer = KafkaProducer(bootstrap_servers=[self.serverlist])
            producer.send('oa_qian', str.encode(self.msg))
            producer.flush()
            producer.close(timeout=60)
            return "success"
        except:
            return "error"

if __name__ == '__main__':
    mq_s = Mq_s('kafka.sunqb.com:9092', 'sunqingbiao;sun;890897')
    mq_s.producer_msg()