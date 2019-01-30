from pyquery import PyQuery as pq
import time
import sys
import re
import urllib
import logging
import codecs
import csv
import datetime

log = logging.getLogger()
log.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(logging.Formatter('[%(levelname)s] %(funcName)s: %(message)s'))
log.addHandler(ch)

def parseFile(url_key):
    output = codecs.open(url_key + 'result.csv', 'w', encoding='utf-8-sig') 
    param1 = urllib.parse.quote(url_key.encode('utf-8'))
    f_csv = csv.writer(output)
    
    for i in range(0,50,10):
        print("_______________________begin______________________"+ datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        url = 'http://zhidao.baidu.com/q?ct=17&tn=ikaslist&word='+param1+'&pn='+str(i) 
        try:
            zhidaolist = urllib.request.urlopen(url)
        except:
            log.error('get error ' + url)
            continue
        if(zhidaolist.status == 200):
            log.info('get 200 ' + url)
            content = zhidaolist.read().decode('gbk')
        else:
            log.error('404')
            continue

        doc = pq(content)	
        its=doc("dl").items()

        for it in its:
            iurl = (it("a.ti").attr('href'))
            title = (it("a.ti").text())
            cont = (it("dd.dd.summary").text())
            f_csv.writerow((iurl, title, cont))
        print("_______________________rest______________________"+ datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(3)
    output.close()
    

def main():
    parseFile("这道题")
    parseFile("这题")
    parseFile("题目")
   
    
    
if __name__ == "__main__":
    main()

