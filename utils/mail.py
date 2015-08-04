# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
#
host = 'smtp.exmail.qq.com'
port = '25'

to = ['710270532@qq.com']
cc = ['daodaozhanhou@163.com']#抄送
bcc = []#密送

subject = 'python邮件测试'#设置主题
content = u'''python邮件测试内容,怎么就能不成功，怎么就垃圾邮件了，
快成功吧。标题也也有、写了这么多字还垃圾邮件，你逗我'''

sender = 'hongwei.zhang@fengyunzhibo.com'
username = 'hongwei.zhang@fengyunzhibo.com'
password = '001gujingwubo'


class Mail:
	def _init_():
		message = MIMEText(content, _subtype='html', _charset='utf-8')#创建一个html格式邮件的实例
		message['Subject'] = subject
		message['From'] = '<'+sender+'>'
		message['To'] = ';'.join(to)
		message['Cc'] = ';'.join(cc)
		message['Bcc'] = ';'.join(bcc)

		server = smtplib.SMTP(host, port)
		server.set_debuglevel(False)#False/True
		server.login(username, password)
		server.sendmail(sender, to+cc+bcc, message.as_string())
		server.quit()
		print 'send simple email success'