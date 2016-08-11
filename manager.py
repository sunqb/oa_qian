#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import os
from flask.ext.script import Server,Manager
from app.oa_qian import app

# 编码
reload(sys)
sys.setdefaultencoding('utf8')

manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=9123))

@manager.command
def oa():
    print "running..."

if __name__ == "__main__":
    manager.run()

