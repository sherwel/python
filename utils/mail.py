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
			#创建一个html格式邮件的实例
			message = MIMEText(_text=content, _subtype='html', _charset='utf-8')
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

	def sendMultipartMail(self, subject, content, attachment, to, cc, bcc):
		try:
			#创建一个带附件格式邮件的实例
			message = MIMEMultipart()
			message['Subject'] = subject
			message['From'] = '<'+self.sender+'>'
			message['To'] = ';'.join(to)
			message['Cc'] = ';'.join(cc)
			message['Bcc'] = ';'.join(bcc)

			#添加附件
			if attachment is not None:
				for filename in attachment:
					path = attachment[filename]
					attach = MIMEText(_text=open(path, 'rb').read(), _subtype='base64', _charset='utf-8')
					attach["Content-Type"] = 'application/octet-stream'
					attach["Content-Disposition"] = 'attachment; filename="'+filename.encode('gbk')+'"'#解决附件名中文乱码
					message.attach(attach)
			server = smtplib.SMTP(self.host, self.port)
			server.set_debuglevel(True)#False/True
			server.login(self.username, self.password)
			server.sendmail(self.sender, to+cc+bcc, message.as_string())
			server.quit()
			return True
		except Exception,e:
			print e
			return False