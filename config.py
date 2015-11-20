__author__ = 'Junko'
# -*- coding: utf-8 -*-

import json
import pachong
import importDB
import getAllList
import threading


def getMainJson():
    dir = open('\\pytmp\\config\\main.json', 'r').read()
    value = json.loads(dir)
    return value


def getConfigJson():
    i = open('\\pytmp\\config\\config.json', 'r').read()
    rang = json.loads(i)

    return rang

# def callPachong():
#     for code in range(int(getConfigJson()["config"][0]["start"]), int(getConfigJson()["config"][0]["end"])):
#         pachong.getCsv(str(code))
#         importDB.inserData(str(code))
#         time.sleep(1)

def getDbInfo():
    data = open('data\\config\\mysql.json', 'r').read()
    value = json.loads(data)
    return value


def callPachong_Sh():
     getAllList.getShList()
     # getAllList.getShList()
     # db = MySQLdb.connect(host=getDbInfo()["MYSQL"][0]["host"],user=getDbInfo()["MYSQL"][0]["user"],passwd=getDbInfo()["MYSQL"][0]["passwd"],db=getDbInfo()["MYSQL"][0]["db"])
     list = open('data\\list\\shlist.txt', 'r').read()
     # con = db.cursor()
     for code in list.split(','):
         # sql = 'SELECT DISTINCT 1 FROM getdata WHERE CODE = \'\\'+'\''+code+'\''
         # con.execute(sql)
         # d = con.fetchone()
         # if d != 1:
         #     pachong.getCsv(code)
         #     importDB.inserData(code)
         #     # return 'Done!'
         # else:
         #     return 'DB has this code!'
         pachong.getCsv(code)
         importDB.inserData(code)
     # db.close()


def callPachong_Sz():
     getAllList.getSzList()
     # getAllList.getShList()
     # db = MySQLdb.connect(host=getDbInfo()["MYSQL"][0]["host"],user=getDbInfo()["MYSQL"][0]["user"],passwd=getDbInfo()["MYSQL"][0]["passwd"],db=getDbInfo()["MYSQL"][0]["db"])
     list = open('data\\list\\szlist.txt', 'r').read()
     # con = db.cursor()
     for code in list.split(','):
         # sql = 'SELECT DISTINCT 1 FROM getdata WHERE CODE = \'\\'+'\''+code+'\''
         # con.execute(sql)
         # d = con.fetchone()
         # if d != 1:
         #     pachong.getCsv(code)
         #     importDB.inserData(code)
         #     # return 'Done!'
         # else:
         #     return 'DB has this code!'
         pachong.getCsv(code)
         importDB.inserData(code)
     # db.close()

threads = []
t1 = threading.Thread(target=callPachong_Sh)
threads.append(t1)
t2 = threading.Thread(target=callPachong_Sz)
threads.append(t2)


if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
