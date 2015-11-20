__author__ = 'Junko'
 # -*- coding: utf-8 -*-

import pachong
import MySQLdb
import json
import config
import os


def csvAnalytical(code):
    file_object = open('data\\datatmp\\'+code+'.csv', 'r')
    value=[]
    # file = open('D:\\tmp\\123.txt', 'r',coding='utf-8')
    line = file_object.readlines()
    for i in line:
        value.append(tuple(i.decode('gbk').split(',')))
    file_object.close()
    del value[0]
    return value

def getDbInfo():
    data = open(r'data//config//mysql.json', 'r').read()
    value = json.loads(data)
    return value

def inserData(code):
    db = MySQLdb.connect(host=getDbInfo()["MYSQL"][0]["host"],user=getDbInfo()["MYSQL"][0]["user"],passwd=getDbInfo()["MYSQL"][0]["passwd"],db=getDbInfo()["MYSQL"][0]["db"], charset="utf8")
    con = db.cursor()
    sql = r'insert into getdata (data_dt,code,nam,spj,hight,low,kpj) values (%s,%s,%s,%s,%s,%s,%s)'
    if os.path.exists('data\\datatmp\\'+code+'.csv'):
        n = con.executemany(sql, csvAnalytical(code))
    db.commit()
    con.close()
    db.close()


if __name__ == '__main__':
    print inserData(str('603999'))
