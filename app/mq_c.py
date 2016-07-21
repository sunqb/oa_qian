#!/usr/bin/python
# -*- coding: UTF-8 -*-
#重新设置编码
import sys
import logging as log
from kafka import KafkaConsumer

reload(sys)
sys.setdefaultencoding('utf8')

#log.basicConfig(level=log.DEBUG)

def consumer_msg(serverlist):
    consumer = KafkaConsumer('oa_qian',
                         group_id='my-group',
                         bootstrap_servers=[serverlist])
    for message in consumer:
        print message.value

if __name__ == '__main__':
    consumer_msg('kafka.sunqb.com:9092')