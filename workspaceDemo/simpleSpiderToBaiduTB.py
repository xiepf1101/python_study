#coding=utf-8

#简单爬取百度贴吧内容

from bs4 import BeautifulSoup
import requests
import lxml

#百度贴吧
url = "https://tieba.baidu.com/p/3572475102"
html = requests.get(url).content
soup = BeautifulSoup(html, 'lxml')

article = soup.find("div", class_="left_section")

#在正文标签里面找图片链接
article1 = article.find_all()

images = article.find_all('img', class_="BDE_Image")

#下载图片
i=0
print("start")

for image in images:
    image_url = image["src"]
    #获取图片url
    
    with open("D:/thisme_D/Python/workspace/python_study_file/百度贴吧/"+str(i)+".jpg", 'wb') as f:
        try:
            re = requests.get(image_url).content
            f.write(re)
            print(str(i)+".jpg images is downloading")
            i+=1
        except Exception:
            print("error")

print("image downloading finish")

#百度贴吧   发帖标题和内容
title = article.find('div',class_="core_title_wrap_bright clearfix")
#find_all搜索得到的是列表，不能直接用find查找其中的标签
endTitle = title.find('h3')

content = article.find_all('div',class_="d_post_content j_d_post_content ")
print("start")

user_card = article.find_all("a",class_="p_author_name j_user_card")


allContent = "";

#多行注释 """内容"""
#两种集合遍历的方式
"""
for cont in content:
    try:
        allContent += str(cont.get_text())+"\n"
    except Exception:
        print("error")
"""    

for i in range(0,len(content)):
    try:
        allContent += str(user_card[i].get_text())+":\n"+str(content[i].get_text())+"\n"
    except Exception:
        print("error")

#创建文件写在循环内部会导致前面写入的被覆盖
with open("D:/thisme_D/Python/workspace/python_study_file/百度贴吧/"+str(endTitle["title"])+".txt", "w") as f:
    f.write(allContent)
   
print("success")



#搜索百度贴吧    采集吧中内容

keyword = "秋"
url = "https://tieba.baidu.com/f?ie=utf-8&kw="+keyword
html = requests.get(url).content
soup = BeautifulSoup(html, "lxml")
#print(soup)

th_tit = soup.find_all("a", "j_th_tit")
href = "https://tieba.baidu.com"
for tit in th_tit:
    print(href+tit["href"])

#print(str(th_tit))
