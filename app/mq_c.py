#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 重新设置编码
import sys
import logging as log
from kafka import KafkaConsumer

reload(sys)
sys.setdefaultencoding('utf8')


# log.basicConfig(level=log.DEBUG)

def consumer_msg(serverlist):
    consumer = KafkaConsumer('oa_qian',
                             group_id='my-group',
                             bootstrap_servers=[serverlist])
    for message in consumer:
        msg = bytes.decode(message.value)
        msglist = msg.split(";")
        username = msglist[0]
        password = msglist[1]
        key = msglist[2]
        type = msglist[3]
        # TODO 调用签到代码，这里需要将生产者配置为必须返回ack模式，否则无法收到客户端回执


if __name__ == '__main__':
    consumer_msg('kafka.sunqb.com:9092')
