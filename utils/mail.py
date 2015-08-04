# -*- coding: utf-8 -*-
import smtplib


host = 'smtp.qq.com'
port = '25'

to = '710270532.qq.com'
bc = ''#密送
cc = ''#抄送
message = 'python邮件测试内容'

sender = 'hongwei.zhang@fengyunzhibo.com'
username = 'daodaozhanhou'
password = '001gujingwubo'

def sendMail():
	server = smtplib.SMTP(host, port)
	server.login(username, password)
	server.sendmail(sender, to, message)