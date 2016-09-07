#!/usr/bin/env python
# -*- coding: utf-8 -*-

' 考勤 '

__author__ = 'sunqb'

import sys
import urllib2
import re
import urllib
import logging as log

# 编码
reload(sys)
sys.setdefaultencoding('utf-8')

# 日志配置
logger = log.getLogger()
logger.setLevel(log.DEBUG)

# 自己的username
myusername = '''sunqingbiao'''


class Attendance:
    def __init__(self, username, password, key):
        self.username = username
        self.password = password
        self.key = key

    def singin(self):
        if (self.username != myusername):
            return "invalidate"
        request = urllib2.Request("http://oa.vemic.com/home/public/dologin")
        request.add_header('User-Agent', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
        request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        request.add_header('Accept-Language', 'en-US,en;q=0.5')
        request.add_header('Host', 'oa.vemic.com')
        values = {'username': self.username, 'password': self.password, 'dynamickey': self.key}
        oa_data = urllib.urlencode(values)

        response = urllib2.urlopen(request, data=oa_data, timeout=3)

        result = response.read()
        html = result.decode('utf8')
        pattern = re.compile(
            r'<input type="tel" id="dynamickey" name="dynamickey" maxlength="6" style="width:80px;" value="(.*?)" autocomplete="off" />',
            re.S)
        items = re.findall(pattern, html)
        if (len(items) > 0):
            return "error"
        else:
            return "success"

    def singout(self):
        if (self.username != myusername):
            return "invalidate"
        request = urllib2.Request("http://oa.vemic.com/home/public/dosignoff")
        request.add_header('User-Agent', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
        request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        request.add_header('Accept-Language', 'en-US,en;q=0.5')
        request.add_header('Host', 'oa.vemic.com')
        values = {'username': self.username, 'password': self.password, 'dynamickey': self.key}
        oa_data = urllib.urlencode(values)

        response = urllib2.urlopen(request, data=oa_data, timeout=3)

        result = response.read()
        html = result.decode('utf8')
        dicdata = eval(html)
        if (dicdata.get("status") == 0):
            return "error"
        else:
            return "success"

    def log_record(self, username, signtype):
        request = urllib2.Request("http://oa.sunqb.com/logrecord")
        request.add_header('User-Agent', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
        request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        request.add_header('Accept-Language', 'en-US,en;q=0.5')
        request.add_header('Host', 'oa.sunqb.com')
        values = {'username': username, 'type': signtype}
        log_data = urllib.urlencode(values)
        try:
            response = urllib2.urlopen(request, data=log_data, timeout=3)
            result = response.read()
            html = result.decode('utf8')
            if (html == 'logsuccess'):
                return '''logsuccess'''
            else:
                return '''logerror'''
        except Exception as e:
            return e


# if __name__ == '__main__':
# oa = Attendance()
