# -*- coding: utf-8 -*-

from utils import mongo

connection = mongo.MongoConnection(port=27017, host='localhost', databaseName='test', replicaSet=None)
result = connection.auth(username='root', password='root')

if result==True:
	print 'mongodb connection success'
else:
	print 'mongodb connection fail'
