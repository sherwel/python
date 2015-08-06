# -*- coding: utf-8 -*-

from pymongo import MongoClient

class MongoConnection():
	def __init__(self, port=27017, host='localhost', databaseName='test', replicaSet=None):
		if replicaSet!=None:
			client = MongoClient(host=host, port=port, replicaSet=replicaSet)
		else:
			client = MongoClient(host=host, port=port)
		self.db = client[databaseName]

	def auth(self, username='root', password='root'):
		return self.db.authenticate(username, password)


	def insert(self, collectionName, document):
		posts = self.db.posts
		_id = posts.insert(document)
		return _id

	def delete(self, collectionName):
		collection = self.db[collectionName]

	def find(self, collectionName):
		collection = self.db[collectionName]

	def update(self, collectionName):
		collection = self.db[collectionName]
