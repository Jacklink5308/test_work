#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import pymysql
from pprint import *

cnn = pymysql.connect(host = '127.0.0.1',
                      user = 'root',
                      passwd = '4394wt35',
                      db = 'test1',
                      charset = 'utf8')
c = cnn.cursor()
c.execute('select * from coustomers;')
rows = c.fetchall()
print(rows)
c.execute('show create table coustomers')
a = c.fetchall()
pprint(a)
c.close()
