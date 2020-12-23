# oa_qian这个目录为新的python解释器目录
- 在这个目录下面可以开发
- kafka.sunqb.com 需要配置成自己的kafka服务地址
- 消息协议：username+";"+password+";"+"key"+";"+type (1表示签到，2表示签退)
- 服务上启动(不使用uwsgi)： python manager.py runserver
- 客户端运行：安装python2.7,安装kafka-python。在attendance里面需要把myusername配置为自己的用户名，例如： myusername = '''sunqingbiao'''。把mq_c里面的my-group替换成自己的用户名
```
CREATE TABLE `t_oa_record` (
  `rec_id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '记录ID，主键',
  `username` VARCHAR(100) NULL COMMENT '用户名',
  `signtype` INT(11) NOT NULL COMMENT '签到类型：1签到，2签退',
  `add_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '添加时间',
  PRIMARY KEY (`rec_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COMMENT='签到记录表';
```
