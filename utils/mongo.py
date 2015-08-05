# -*- coding: utf-8 -*-

from pymongo import MongoClient

class MongoConnection():
	def __init__(self, _port=27017, _host='localhost', _databaseName='test', _username='root', _password='root'):
		client = MongoClient(_host, _port)
		self.db = client[_databaseName]
		print self.db.authenticate(_username, _password)

	def insert(self, collectionName):
		collection = self.db[collectionName]

	def delete(self, collectionName):
		collection = self.db[collectionName]

	def find(self, collectionName):
		collection = self.db[collectionName]

	def update(self, collectionName):
		collection = self.db[collectionName]
