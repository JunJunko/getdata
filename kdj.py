#-*- coding: UTF-8 -*-
__author__ = 'Junko'

import MySQLdb
import json
import numpy as np

data = []

def getDbInfo():
    data = open(r'data//config//mysql.json', 'r').read()
    value = json.loads(data)
    return value

def getDict(code):
    db = MySQLdb.connect(host=getDbInfo()["MYSQL"][0]["host"],user=getDbInfo()["MYSQL"][0]["user"],passwd=getDbInfo()["MYSQL"][0]["passwd"],db=getDbInfo()["MYSQL"][0]["db"])
    con = db.cursor()
    sql = r'select DATE_FORMAT(data_dt,'+'\'%Y%m%d\''+'),  hight, low, spj, code from getdata where  spj > 0 and code ='+code+' order by 1'
    con.execute(sql)
    for row in con.fetchall():
        data.append(list(row))
    return data


def KDJ(date,N=9,M1=3,M2=3):
    datelen=len(date)
    array=np.array(date)
    kdjarr=[]
    for i in range(datelen):
        if i-N<0:
            b=0
        else:
            b=i-N+1
        rsvarr=array[b:i+1,0:5]
        rsv=round((float(rsvarr[-1,-1])-float(min(rsvarr[:,-2])))/(float(max(rsvarr[:,-3]))-float(min(rsvarr[:,-2])))*100,2)
        # spj = rsvarr[-1,-1]
        # low = rsvarr[:,-2]
        # hight = rsvarr[:,-3]
        if i==0:
            k=rsv
            d=rsv
        else:
            k=round(1/float(M1)*rsv+(float(M1)-1)/M1*float(kdjarr[-1][2]),2)
            d=round(1/float(M2)*k+(float(M2)-1)/M2*float(kdjarr[-1][3]),2)
            # 当日K值=2/3×前一日K值+1/3×当日RSV
            # 当日D值=2/3×前一日D值+1/3×当日K值
        j=round(3*k-2*d,2)
        kdjarr.append(tuple((rsvarr[-1,0],rsv,k,d,j)))
    # return kdjarr
    db = MySQLdb.connect(host=getDbInfo()["MYSQL"][0]["host"],user=getDbInfo()["MYSQL"][0]["user"],passwd=getDbInfo()["MYSQL"][0]["passwd"],db=getDbInfo()["MYSQL"][0]["db"])
    con = db.cursor()
    sql = r'insert into kdj (data_dt, kdj_rsv, kdj_k, kdj_d, code) values (%s,%s,%s,%s,%s,%s)'
    n = con.executemany(sql, kdjarr)
    db.commit()
    con.close()
    db.close()

#     n日RSV=（Cn－Ln）/（Hn－Ln）×100
# 公式中，Cn为第n日收盘价；Ln为n日内的最低价；Hn为n日内的最高价。


if __name__ == "__main__":
    print KDJ(getDict('000001'))
    # print getDict('000001')