#coding=utf-8

#print(soup.prettify()) # 格式化输出网址源码

# 打印title，用soup加标签名轻松获得标签内容，而不需要用正则表达式
    #print(soup.title)
    #print(soup.head)
    #print(soup.p)  #只打印第一个p的部分
    #print(soup.div.attrs) # 打印div标签的所有属性，得到的类型是一个字典
    #print(soup.div['class']) # 但单独打印div的某一个部分
    #print(soup.title.string)  # .string获得标签内部的文字

# 遍历文档树
# 直接子节点 .contents  .children
    #print('直接子节点')
    #for child in soup.body.children :
     #   print(child)
# 用来遍历
# 所有子孙节点 .descendans   包括其内部所有内容
    #print('所有子孙节点')
    #for child in soup.body.descendants:
    #   print(child)
# 所有父节点 .parents
# 所有兄弟节点 .next_siblings   .previous_siblings
# 所有前后节点 .next_elements  .previous_elements

# 节点内容 .string (s)s

# 搜索文档树
# 注意：如果一个指定名字的参数不是搜索内置的参数名,
# 搜索时会把该参数当作指定名字tag的属性来搜索,
# 如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性


from bs4 import BeautifulSoup
import requests

url = 'http://m.ximalaya.com/news/2018-04-19/VUzfwQde.html'

#获取网址源码
html = requests.get(url).text
print(html)
soup = BeautifulSoup(html, 'lxml')

print('开始抓取')

title = soup.title.string
with open("D:/thisme_D/Python/workspace/python_study_file/"+title+'.txt', 'w') as f:
    href = soup.find_all('p')
    try:
        f.write('\t%s\r\n' %str(title)) #前面%s 后面之间空格加%内容
        for hre in href:
            if(hre.string!=None):       #未解决标签内容回车后打印none问题
                f.write('\t%s\r\n' %str(hre.string))
    except Exception:
        print('发生错误')
print('抓取成功')


#爬取豆瓣河神演员照片列表

from bs4 import BeautifulSoup
import requests
import lxml
import re

url = 'https://movie.douban.com/subject/26776350/celebrities'
html = requests.get(url).content
soup = BeautifulSoup(html, 'lxml')

#用class搜索，由于是python的关键词， 所以用下划线
imgs = soup.find_all(class_="avatar")
names = soup.find_all('a',href=re.compile('celebrity'),class_="name")

i = 0
print("开始下载")

for img in imgs:
    img_url = img['style']
    #利用切片获取图片网址
    img_content = img_url.split('(')[1].split(')')[0]
    try:
        print("下载第%s涨图片"%i)
        with open("D:/thisme_D/Python/workspace/python_study_file/河神/"+str(names[i].string)+".jpg",'wb') as f:
            #将获得图片网址转换成二进制编码
            f.write(requests.get(img_content).content)
            i+=1
    except Exception:
        print("出现错误")

print("下载完成")