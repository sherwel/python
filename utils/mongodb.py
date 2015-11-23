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


	#增
	def insert(self, collectionName, document):
		collection = self.db[collectionName]
		_id = collection.insert(document)
		return _id

	def insertMany(self, collectionName, documents, ordered=True):
		collection = self.db[collectionName]
		collection.insert_many(documents, ordered)


	#删
	def delete(self, collectionName, filter):
		collection = self.db[collectionName]
		collection.delete_one(filter)

	def deleteMany(self, collectionName, filter):
		collection = self.db[collectionName]
		collection.delete_many(filter)

	#查
	def find(self, collectionName, document):
		collection = self.db[collectionName]
		return collection.find_one(document)

	def findMany(self, collectionName, document):
		collection = self.db[collectionName]
		return collection.find(document)

	def count(self, collectionName, document):
		collection = self.db[collectionName]
		return collection.find(document).count()

	#改
	def update(self, collectionName, filter, update, upsert=False):
		collection = self.db[collectionName]
		collection.update_one(filter, update, upsert)

	def updateMany(self, collectionName, filter, update, upsert=False):
		collection = self.db[collectionName]
		collection.update_many(filter, update, upsert)
