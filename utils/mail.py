# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Mail():
	def __init__(self, port, host, sender, username, password):
		self.port = port
		self.host = host
		self.sender = sender
		self.username = username
		self.password = password
		
	def sendSimpleMail(self, subject, content, to, cc, bcc):
		try:
			message = MIMEText(content, _subtype='html', _charset='utf-8')#创建一个html格式邮件的实例
			message['Subject'] = subject
			message['From'] = '<'+self.sender+'>'
			message['To'] = ';'.join(to)
			message['Cc'] = ';'.join(cc)
			message['Bcc'] = ';'.join(bcc)

			server = smtplib.SMTP(self.host, self.port)
			server.set_debuglevel(False)#False/True
			server.login(self.username, self.password)
			server.sendmail(self.sender, to+cc+bcc, message.as_string())
			server.quit()
			return True
		except Exception,e:
			return False

	def sendMultipartMail(self, subject, filename, content, to, cc, bcc):
		try:
			message = MIMEMultipart()#创建一个带附件格式邮件的实例
			message['Subject'] = subject
			message['From'] = '<'+self.sender+'>'
			message['To'] = ';'.join(to)
			message['Cc'] = ';'.join(cc)
			message['Bcc'] = ';'.join(bcc)

			attach = MIMEText(open('d:\\123.text', 'rb').read(), 'base64', 'gb2312')
			attach["Content-Type"] = 'application/octet-stream'
			attach["Content-Disposition"] = 'attachment; filename="'+filename+'"'
			message.attach(attach)


			server = smtplib.SMTP(self.host, self.port)
			server.set_debuglevel(False)#False/True
			server.login(self.username, self.password)
			server.sendmail(self.sender, to+cc+bcc, message.as_string())
			server.quit()
			return True
		except Exception,e:
			return False