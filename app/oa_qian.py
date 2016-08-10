#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 重新设置编码
import sys
from flask import Flask
from flask import request
from flask import render_template
from mq_s import Mq_s

#编码
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)


# 首页
@app.route('/', methods=['GET', 'POST'])
def home():
    return '''<h1 style='text-align:center'>欢迎使用OA考勤系统</h1><br/><p style='text-align:center'><a  href='/sign'>签到</a></p><p style='text-align:center'><a href='/unsign'>签退</a></p>'''


# 跳转到签到页
@app.route('/sign', methods=['GET'])
def singnin_form():
    return '''<form action="/sign" method="post">
              <h3 style="text-align:center">签到页</3>
              <p>账号&nbsp&nbsp<input name="username" /></p>
              <p>密码&nbsp&nbsp<input name="password" type="password" /></p>
              <p>密钥&nbsp&nbsp<input name="key" /></p>
              <p><button type="submit">Submit</button></p>
            '''


# 签到
@app.route('/sign', methods=['POST'])
def sign_in():
    # 需要从request对象读取表单内容：
    username = request.form['username']
    password = request.form['password']
    key = request.form['key']
    mq_s = Mq_s('kafka.sunqb.com:9092', username + ';' + password + ';' + key + ';1')
    print mq_s.producer_msg()
    return '''<h3>签到成功，<a href='/'>点此返回</a></h3>'''


# 跳转到签退页
@app.route('/unsign', methods=['GET'])
def singnout_form():
    return '''<form action="/unsign" method="post">
              <h3 style="text-align:center">签退页</3>
              <p>域账号 <input name="username" /></p>
              <p>密码 <input name="password" type="password" /></p>
              <p>动态密钥 <input name="key" /></p>
              <p><button type="submit">Submit</button></p>
            '''


# 签退
@app.route('/unsign', methods=['POST'])
def sign_out():
    # 需要从request对象读取表单内容：
    username = request.form['username']
    password = request.form['password']
    key = request.form['key']
    mq_s = Mq_s('kafka.sunqb.com:9092', username + ';' + password + ';' + key + ';2')
    print mq_s.producer_msg()
    return '''<h3>签退成功，<a href='/'>点此返回</a></h3>'''


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):  # 如果没有None 那么不带参数就报错了
    return render_template('hello.html', name=name)

    # if __name__ == '__main__':
    #    app.run(host='localhost', port=9000, debug=True)
