# -*- coding: utf-8 -*-

import mysql.connector

class MysqlConnection():
    def __init__(self, user='root', password='root', port='27017', host='localhost', database='test'):
        self.connection = mysql.connector.connect(user='root', password='root', port='3306', host='localhost', database='test')
