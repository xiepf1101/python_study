#coding=utf-8

import requests
import os
import time

url = 'http://www.baidu.com'

while True:
    try:
        data = requests.get(url).text
        print("connection success")
        time.sleep(300)
    except:
        print('connection failed')
        b = os.popen('sayHelloBat.bat')
        b.read()    
        time.sleep(60)