#coding=utf8
import time
# -*- coding: utf-8 -*-
# *********************************
#        自动签到某网站
#       vresion：python 2
#         author:张琼
#       西北农林科技大学 计算机141
# *********************************
#from urllib import request,parse
import cookielib
import urllib
import urllib2
import time
# import re
# import io
# from PIL import Image
# import pytesseract
# import requests
#模拟登录测试模块
# print('loging info my ssfw')

while True:

    # time.sleep(3)

    cookie=cookielib.CookieJar()#储存获取到的cookie
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

    loging_data=urllib.urlencode([
        ('email',"xx@qq.com"),
        ('passwd',"xx"),
        ('remember_me','week')])#POST用到的数据

    #请求头
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Host' : 'free.hwss.pw',
        # 'Origin':'http://free.hwss.pw',
        'Accept' :'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        # 'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer' : 'http://free.hwss.pw/user/login.php',
        # Cookie:	user_pwd=b34c9391df229cd8a2a3a1c9d8c77cb8e489349c312f6; uid=429; user_email=804194244%40qq.com; __cfduid=d8ef321cdcb20f2206c28f8e37dc4e4d91486381093; PHPSESSID=m5s0fkchm31bvs76sqo3nt4tb2',
        'Connection' : 'keep-alive',
        # 'X-Requested-With':'XMLHttpRequest',
        # 'Content-Length':'57',
        # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Upgrade-Insecure-Requests':'1',
        # 'Cache-Control':'max-age=0'
    }

    #构造request
    req=urllib2.Request(url='http://free.hwss.pw/user/_login.php',
                        data=loging_data.encode(encoding='utf-8'),
                        headers=headers)
    try:
        # req1 = session.post('http://ss.hwss.pw/user/login.php', data=loging_data, headers=headers)
        result=opener.open(req)#访问请求的链接

        print 'tttttttttttt'
        # print(result.read().decode('utf-8'))
    except urllib2.HTTPError:
        print("connect failed")
    try:
        # print '1111'
        # session.get('http://ss.hwss.pw/checkin.php', headers=headers)
        # result=opener.open('http://free.hwss.pw/user/index.php')#进入教务系统个人成绩信息界面
        # print '2222'
        req=urllib2.Request(url='http://free.hwss.pw/user/_checkin.php',
                        data=loging_data.encode(encoding='utf-8'),
                        headers=headers)
        result2=opener.open(req)
        # print (result2.read().decode('utf-8'))
        print "ck1"
        #print(result.read().decode('utf-8'))
        #page=result.read()
        #print (page)
        # f=file("score.html","w") #写入一个html文件
        # f.write(page)
        # f.close()


    except Exception,e:
        print str(e)

    print "1 finished,plz wait"
    time.sleep(86401)
