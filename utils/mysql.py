# -*- coding: utf-8 -*-

import mysql.connector

class MysqlConnection():

	def __init__(self, port=27017, host='localhost', databaseName='test', replicaSet=None):
		if replicaSet!=None:
			client = MongoClient(host=host, port=port, replicaSet=replicaSet)
		else:
			client = MongoClient(host=host, port=port)
		self.db = client[databaseName]

	def auth(self, username='root', password='root'):
		return self.db.authenticate(username, password)

connection = mysql.connector.connect(user='root', password='root', port='3306', host='localhost', database='test')

print connection