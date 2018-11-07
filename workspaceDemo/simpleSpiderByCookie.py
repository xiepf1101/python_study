#coding=utf-8

#爬去知乎   headers的应用

from http import cookiejar
from urllib import request
from bs4 import BeautifulSoup

# # cookie的测试
# # 声明一个CookieJar实例对象
cookie = cookiejar.CookieJar()
# # 创建cookie处理器
handle = request.HTTPCookieProcessor(cookie)
# # 通过cookie处理器创建opener实例
opener = request.build_opener(handle)
# # 通过opener实例打开网页
response = opener.open('https://www.zhihu.com/question/25313930')
# # 打印cookie
for item in cookie:
     print('Name = %s' % item.name)
     print('Value = %s' % item.value)

#命名保存cookie的文件和文件名
filename = 'D:\cookie.txt'
#保存cookie到文件
def saveCookie():
     cookie = cookiejar.MozillaCookieJar(filename)
     handler = request.HTTPCookieProcessor(cookie)
     opener = request.build_opener(handler)
     response = opener.open('https://www.zhihu.com/question/25313930')
     # ignore_discard的意思是即使cookies将被丢弃也将它保存下来；
     # ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入     
     cookie.save(ignore_discard=True, ignore_expires=True)

saveCookie()
#从文件中获取cookie并访问
#创建MozillaCookirjar实例
cookie = cookiejar.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load(filename,ignore_discard=True,ignore_expires=True)
#创建cookie处理器
handle = request.HTTPCookieProcessor(cookie)
#通过cookie处理器创建opener对象
opener = request.build_opener(handle)
#通过opener对象的open方法打开网页
response = opener.open('https://www.zhihu.com/question/25313930')
html = response.read()

#解析html
soup = BeautifulSoup(html, 'lxml')
storys = soup.find_all('div',class_="List-item")
print(len(storys))
for story in storys:
     print(story)
     nameLabel = story.find('meta', itemprop="name")
     name = nameLabel["content"]
     with open("D:/thisme_D/Python/workspace/python_study_file/"+str(name)+'.txt', 'w') as f:
          storyText = story.find('span', class_="RichText ztext CopyrightRichText-richText")
          #storyPages = storyText.find_all('p')
          try:
               #获取多个内容，不过需要遍历获取，比下：
               for string in storyText.strings:
                    f.write(repr(string)+"\n")
               print("D:\thisme_D\Python\workspace\python_study_file"+str(name)+' has been finished')
          except Exception:
               print('Something is wrong on writing to txt')
print('That is all')


soup = BeautifulSoup(html, 'lxml')

with open("D:/thisme_D/Python/workspace/python_study_file/html_.txt", 'w') as f:
     try:
          f.write(str(html)+"\n")
     except Exception:
          print('Something is wrong on writing to txt')

storys = soup.find_all('div',class_="ContentItem AnswerItem")
print(len(storys))
for story in storys:
     print(story)
     nameLabel = story.find('meta', itemprop="name")
     name = nameLabel["content"]
     with open("D:/thisme_D/Python/workspace/python_study_file/"+str(name)+'.txt', 'w') as f:
          storyText = story.find('span', class_="RichText ztext CopyrightRichText-richText")
          #storyPages = storyText.find_all('p')
          try:
               #获取多个内容，不过需要遍历获取，比下：
               for string in storyText.strings:
                    f.write(repr(string)+"\n")
               print("D:\thisme_D\Python\workspace\python_study_file"+str(name)+' has been finished')
          except Exception:
               print('Something is wrong on writing to txt')
print('That is all')