# -*- coding: utf-8 -*-

from utils import mysqldb

insert = 'insert into user(username, password) values(\'root\', \'root\')'
delete = 'delete from user where id=7'
select = 'select * from user'
update = 'update user set username=\'hongwei\' where id=8'

try:
    connection = mysqldb.MysqlConnection(user='root', password='root', port=3306, host='localhost', database='test', charset='utf8')
#     result = connection.insert(insert)
#     result = connection.count(select)
#     result = connection.delete(delete)
#     result = connection.update(update)
#     print result
except Exception as e:
    print e