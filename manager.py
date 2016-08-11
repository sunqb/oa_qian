#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import os
from app.oa_qian import app
from flask.ext.script import Manager, Server

if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

# 编码
reload(sys)
sys.setdefaultencoding('utf8')

manager = Manager(app)
manager.add_command("runserver",
                    Server(host="127.0.0.1", port=9123, use_debugger=True))

if __name__ == '__main__':
    manager.run()
