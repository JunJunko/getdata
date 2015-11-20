__author__ = 'Junko'
# -*- coding: utf-8 -*-


import urllib2
import re


def getWebData():
    url = r'http://quote.eastmoney.com/stocklist.html'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request).read()
    return response


def getShList():
    patter = '<li><a target="_blank" href="http://quote.eastmoney.com/sh6.*?.html">.*?\((.*?)\)</a></li>'
    mindate = re.findall(patter, getWebData())
    f = open('data\\list\\shlist.txt', 'wb')
    for i in mindate:
            f.write(i+',')
    f.close()

def getSzList():
    patter = '<li><a target="_blank" href="http://quote.eastmoney.com/sz00.*?.html">.*?\((.*?)\)</a></li>'
    mindate = re.findall(patter, getWebData())
    f = open('data\\list\\szlist.txt', 'wb')
    for i in mindate:
            f.write(i+',')
    f.close()

if __name__ == '__main__':
    getShList()
    getSzList()