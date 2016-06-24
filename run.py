#!/usr/bin/python
# -*- coding: UTF-8 -*-
#重新设置编码
import sys
from app.oa_qian import app

reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == '__main__':
    app.run(host='localhost', port=9123, debug=True)