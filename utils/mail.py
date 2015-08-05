# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Mail():
	def __init__(self, _port, _host, _sender, _username, _password):
		self._port = _port
		self._host = _host
		self._sender = _sender
		self._username = _username
		self._password = _password
		
	def sendSimpleMail(self, _subject, _content, _to, _cc, _bcc):
		try:
			#创建一个html格式邮件的实例
			message = MIMEText(_text=_content, _subtype='html', _charset='utf-8')
			message['Subject'] = _subject
			message['From'] = '<'+self._sender+'>'
			message['To'] = ';'.join(_to)
			message['Cc'] = ';'.join(_cc)
			message['Bcc'] = ';'.join(_bcc)

			server = smtplib.SMTP(self._host, self._port)
			server.set_debuglevel(False)#False/True
			server.login(self._username, self._password)
			server.sendmail(self._sender, _to+_cc+_bcc, message.as_string())
			server.quit()
			return True
		except Exception,e:
			return False

	def sendMultipartMail(self, _subject, _content, _attachment, _to, _cc, _bcc):
		try:
			#创建一个带附件格式邮件的实例
			message = MIMEMultipart()
			message['Subject'] = _subject
			message['From'] = '<'+self._sender+'>'
			message['To'] = ';'.join(_to)
			message['Cc'] = ';'.join(_cc)
			message['Bcc'] = ';'.join(_bcc)

			#添加附件
			if _attachment is not None:
				for filename in _attachment:
					path = _attachment[filename]
					attach = MIMEText(_text=open(path, 'rb').read(), _subtype='base64', _charset='utf-8')
					attach["Content-Type"] = 'application/octet-stream'
					attach["Content-Disposition"] = 'attachment; filename="'+filename.encode('gbk')+'"'#解决附件名中文乱码
					message.attach(attach)
			server = smtplib.SMTP(self._host, self._port)
			server.set_debuglevel(True)#False/True
			server.login(self._username, self._password)
			server.sendmail(self._sender, _to+_cc+_bcc, message.as_string())
			server.quit()
			return True
		except Exception,e:
			print e
			return False