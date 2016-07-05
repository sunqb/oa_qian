#!/usr/bin/python
# -*- coding: UTF-8 -*-
#重新设置编码
import sys
from flask import Flask
from flask import request
from flask import render_template

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/sign', methods=['GET'])
def singnin_form():
    return '''<form action="/sign" method="post">
              <p>域账号 <input name="username" /></p>
              <p>密码 <input name="password" type="password" /></p>
              <p>动态密钥 <input name="dynamic_key" /></p>
              <p><label><input name="sign_type" type="radio" value="1" />签到 </label> 
<label><input name="sign_type" type="radio" value="0" />签退 </label> </p>
              <p><button type="submit">Submit</button></p>
            '''

@app.route('/sign', methods=['POST'])
def sign_add():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None): #如果没有None 那么不带参数就报错了
    return render_template('hello.html', name=name)

#if __name__ == '__main__':
#    app.run(host='localhost', port=9000, debug=True)