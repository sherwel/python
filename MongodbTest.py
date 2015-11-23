# -*- coding: utf-8 -*-

from utils import mongodb

connection = mongodb.MongoConnection(port=27017, host='localhost', databaseName='test', replicaSet=None)
result = connection.auth(username='root', password='root')

if result==True:
	print 'mongodb connection success'
	_id = connection.insert('python', {"email":"hongwei.zhang@fengyunzhibo.com"})
	print _id

	print connection.find('python',None)
	
else:
	print 'mongodb connection fail'


