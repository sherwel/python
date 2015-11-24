# -*- coding: utf-8 -*-

import mysql.connector

class MysqlConnection():
    def __init__(self, user='root', password='root', port=3306, host='localhost', database='test', charset='utf8'):
        self.connection = mysql.connector.connect(user=user, password=password, port=port, host=host, database=database, charset=charset)
        self.cursor = self.connection.cursor(buffered=True, raw=True)
    #增
    def insert(self, sql):
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            count = self.cursor.rowcount
            if count == 1:
                return True
        except Exception as e:
            print e
            self.connection.rollback()
        finally:
            self.connection.close()
            self.cursor.close()
        return False
    #删
    def delete(self, sql):
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            count = self.cursor.rowcount
            if count!=None and count!=0:
                return True
        except Exception as e:
            print e
            self.connection.rollback()
        finally:
            self.connection.close()
            self.cursor.close()
        return False
    
    #查
    def find(self, sql):
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone()
        except Exception as e:
            print e
        finally:
            self.connection.close()
            self.cursor.close()
        return None
    
    def findMany(self, sql):
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print e
        finally:
            self.connection.close()
            self.cursor.close()
        return None
    
    def count(self, sql):
        try:
            self.cursor.execute(sql)
            return self.cursor.rowcount
        except Exception as e:
            print e
        finally:
            self.connection.close()
            self.cursor.close()
        return None
    
    #改
    def update(self, sql):
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            count = self.cursor.rowcount
            if count!=None and count!=0:
                return True
        except Exception as e:
            print e
            self.connection.rollback()
        finally:
            self.connection.close()
            self.cursor.close()
        return False
