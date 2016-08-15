# oa_qian这个目录为新的python解释器目录
- 在这个目录下面可以开发
- kafka.sunqb.com 需要配置成自己的kafka服务地址
- 消息协议：username+";"+password+";"+"key"+";"+type (1表示签到，2表示签退)
- 客户端运行：在attendance里面需要把myusername配置为自己的用户名，例如： myusername = '''sunqingbiao'''。把mq_c里面的my-group替换成自己的用户名
- 服务上启动 python manager.py runserver