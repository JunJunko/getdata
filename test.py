#-*- coding: UTF-8 -*-

import MySQLdb
import json
import os

# def getDbInfo():
#     data = open(r'D://tmp//pytmp//mysql.json', 'r').read()
#     value = json.loads(data)
#     return value
#
# def test():
#     list = open('data\\list\\shlist.txt', 'r').read()
#     for code in list.split(','):
#          db = MySQLdb.connect(host=getDbInfo()["MYSQL"][0]["host"],user=getDbInfo()["MYSQL"][0]["user"],passwd=getDbInfo()["MYSQL"][0]["passwd"],db=getDbInfo()["MYSQL"][0]["db"])
#          con = db.cursor()
#          sql = 'SELECT 1 FROM getdata WHERE CODE = \'\\'+'\''+code+'\''
#          con = db.cursor()
#          con.execute(sql)
#          print con.fetchone()

if os.path.exists('data\\datatmp\\6032999.csv'):
    print '1'
else:
    print '2'

#
# if __name__ == '__main__':
#     print test()

