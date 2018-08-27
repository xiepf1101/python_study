#coding=utf-8

#根据正则表达式匹配图片     图片文件保存

#以.asp、.jsp、.php 为扩展名，或者有"?"、"="、"%"，以及"&"、"$"、"id"等乱七八糟的字符的网页，都是动态页面 。

#静态网站   .html、.htm、.shtml

import requests    #cmd     #pip install requests
import re

#url = 'http://www.nipic.com/photo/jingguan/ziran/index.html'
url = 'http://www.nipic.com/photo/renwu/nvxing/index.html'

#获取网页源码
data = requests.get(url).text


#图片正则表达式
regex = r'<img src="http://static.nipic.com/images/grey.gif" data-src="(.*?.jpg)"'

#re 是一个列表
pa = re.compile(regex)  #创建一个pa模板，使其符合匹配的网址
ma = re.findall(pa,data) #findall方法 找到data中所有符合pa的对象，添加到re中并返回

#图片的名字
i=0

print('start downloading')

for image in ma :
    i+=1
    print(image)
    image = requests.get(image).content
    print(str(i)+'.jpg')
    
    #\ 要用转义符号\\  表示   要注意元图片的格式
    
    with open('D:/Python/workspace/python_study_file/'+str(i)+'.jpg','wb') as f:
        f.write(image)
        
print('finish downloading')

end = 2

url1 = 'http://www.nipic.com/photo/baike/yule/index.html'

for num in range(1,end+1):
    url=url1+"?page="+str(num)
    print(url) 
    data = requests.get(url).text
    
    pa = re.compile(regex)  
    
    ma = re.findall(pa,data)    
    
    for image in ma :
        i+=1
        image = requests.get(image).content
        
        #\ 要用转义符号\\  表示   要注意元图片的格式
        
        with open('D:/Python/workspace/python_study_file/'+str(i)+'.jpg','wb') as f:
            f.write(image)    