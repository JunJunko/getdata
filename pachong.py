__author__ = 'Junko'

# -*- coding: utf-8 -*-
import urllib2
import urllib
import re


localCSV = r'D:\tmp\pytmp'

def getWebData(code):
    url = r'http://quotes.money.163.com/trade/lsjysj_'+code+'.html'
    if urllib.urlopen(url).getcode() == 200:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request).read()
        return response
    else:
        return '<input type=\"radio\" name=\"date_start_type\" value=\"0\" checked=\"checked\">'+'<input type=\"text\" name=\"date_end_value\" style=\"width:120px\" value=\"0\">'



def getMinDate(code):
    patter = '<input type=\"radio\" name=\"date_start_type\" value=\"(.*?)\" checked=\"checked\">'
    mindate = re.search(patter, getWebData(code))
    return mindate.group(1).replace('-','')

def getMaxDate(code):
    patter = '<input type=\"text\" name=\"date_end_value\" style=\"width:120px\" value=\"(.*?)\">'
    maxdate = re.search(patter, getWebData(code))
    return maxdate.group(1).replace('-','')



def getCsv(code):
    if code[0:1] == '6':
        url = r'http://quotes.money.163.com/service/chddata.html?code='+'0'+code+'&start='+getMinDate(code)+'&end='+getMaxDate(code)+'&fields=TCLOSE;HIGH;LOW;TOPEN'
    else:
        url = r'http://quotes.money.163.com/service/chddata.html?code='+'1'+code+'&start='+getMinDate(code)+'&end='+getMaxDate(code)+'&fields=TCLOSE;HIGH;LOW;TOPEN'
    data = urllib.urlopen(url).read().replace('None','0').replace('\'','0')
    with open('data\\datatmp\\'+code+'.csv', 'wb') as f:
        f.write(data)
    print url


if __name__ == '__main__':
    print getCsv(str("002788"))