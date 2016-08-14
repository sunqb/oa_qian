#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 重新设置编码
import sys
from flask import Flask
from flask import request
from flask import render_template
from mq_s import Mq_s
from util_mysql import Util_mysql

# 编码
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)


# 首页
@app.route('/', methods=['GET', 'POST'])
def home():
    return '''<h1 style='text-align:center'>欢迎使用OA考勤系统</h1><br/><p style='text-align:center'><a  href='/sign'>签到</a></p><p style='text-align:center'><a href='/unsign'>签退</a></p>
    <p style='text-align:center'><a href="/record">记录查询</a></p>'''


# 跳转到签到页
@app.route('/sign', methods=['GET'])
def singnin_form():
    return '''<form action="/sign" method="post">
              <h3 style="text-align:center">签到页</3>
              <p>账号&nbsp&nbsp<input name="username" /></p>
              <p>密码&nbsp&nbsp<input name="password" type="password" /></p>
              <p>密钥&nbsp&nbsp<input name="key" /></p>
              <p><button type="submit">提交</button></p>
            '''


# 签到
@app.route('/sign', methods=['POST'])
def sign_in():
    # 需要从request对象读取表单内容：
    username = request.form['username']
    password = request.form['password']
    key = request.form['key']
    if (len(username) < 1 or len(password) < 1 or len(key) < 1):
        return '''<h3 style='text-align:center'>不允许有值为空，<a href='/'>点此返回</a></h3>'''
    mq_s = Mq_s('kafka.sunqb.com:9092', username + ';' + password + ';' + key + ';1')
    print mq_s.producer_msg()
    return '''<h3 style='text-align:center'>签到成功，<a href='/'>点此返回</a></h3>'''


# 跳转到签退页
@app.route('/unsign', methods=['GET'])
def singnout_form():
    return '''<form action="/unsign" method="post">
              <h3 style="text-align:center">签退页</3>
              <p>账号&nbsp&nbsp<input name="username" /></p>
              <p>密码&nbsp&nbsp<input name="password" type="password" /></p>
              <p>密钥&nbsp&nbsp<input name="key" /></p>
              <p><button type="submit">提交</button></p>
            '''


# 签退
@app.route('/unsign', methods=['POST'])
def sign_out():
    # 需要从request对象读取表单内容：
    username = request.form['username']
    password = request.form['password']
    key = request.form['key']
    if (len(username) < 1 or len(password) < 1 or len(key) < 1):
        return '''<h3 style='text-align:center'>不允许有值为空，<a href='/'>点此返回</a></h3>'''
    mq_s = Mq_s('kafka.sunqb.com:9092', username + ';' + password + ';' + key + ';2')
    print mq_s.producer_msg()
    return '''<h3 style='text-align:center'>签退成功，<a href='/'>点此返回</a></h3>'''


# 跳转到记录查询
@app.route('/record', methods=['GET'])
def record():
    return '''
            <form action="/query-record" method="GET">
                  <h3 style="text-align:center">记录查询页</3>
                  <p>账号&nbsp&nbsp<input name="username" /></p>
                  <p><button type="submit">提交</button></p>
           '''


# 提交记录查询
@app.route('/query-record', methods=['GET'])
def queryRecord():
    pusername = request.args.get('username')
    u_mysql = Util_mysql()
    results = u_mysql.queryRecord(pusername)
    u_mysql.closeconn()
    html = ''''''
    if (len(results) > 0):
        for result in results:
            username = result[1]
            signtype = result[2]
            addtime = result[3]
            if (signtype == '1'):
                signvalue = '''签到'''
            else:
                signvalue = '''签退'''
            html = html + '''
            <p style='text-align:center'>''' + username + '''在''' + addtime + ''' ''' + signvalue + '''</p>
           '''
            print username + signtype + addtime

    else:
        html = '''<p style='text-align:center'>未查询到数据</p>'''
    return html

# 签退
@app.route('/logrecord', methods=['POST'])
def log_record():
    # 需要从request对象读取表单内容：
    username = request.form['username']
    type = request.form['type']
    u_mysql = Util_mysql()
    u_mysql.saveRecord(username, type)
    u_mysql.closeconn()
    if(len(username) <= 0 or len(type) <= 0):
        return '''logerror'''
    else:
        return '''logsuccess'''


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):  # 如果没有None 那么不带参数就报错了
    return render_template('hello.html', name=name)

    # if __name__ == '__main__':
    #    app.run(host='localhost', port=9000, debug=True)
