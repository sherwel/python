# -*- coding: utf-8 -*-

from utils import mail

to = ['710270532@qq.com']
cc = ['daodaozhanhou@163.com']#抄送
bcc = []#密送
subject = u'python邮件测试'#设置主题
content = u'''python邮件测试内容,怎么就能不成功，怎么就垃圾邮件了，
快成功吧。标题也也有、写了这么多字还垃圾邮件，你逗我'''

attachment = {
	u'附件.txt':'D:\\f.txt'
}

email = mail.Mail('25', 'smtp.exmail.qq.com', 'hongwei.zhang@fengyunzhibo.com', 'hongwei.zhang@fengyunzhibo.com', '')
flag = email.sendSimpleMail(subject, content, to, cc, bcc)
if(flag):
	print 'send simple email success'
else:
	print 'send simple email fail'

# flag = email.sendMultipartMail(subject, content, attachment, to, cc, bcc)
# if(flag):
# 	print 'send attachment email success'
# else:
# 	print 'send attachment email fail'