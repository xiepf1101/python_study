#coding=utf-8
#selenium的简单使用

#用法教程#https://cuiqingcai.com/2599.html
#使用文档#https://selenium-python.readthedocs.io/navigating.html

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
#打开请求的url
driver.get('http://www.baidu.com/')
#通过name属性寻找网页元素，此处寻找输入框
elem = driver.find_element_by_name('wd')
#模拟输入Python
elem.send_keys('Python')
#模拟点击回车
elem.send_keys(Keys.RETURN)
#获取网页渲染后的源代码
print(driver.page_source)


# 对于动态加载的网页，例如知乎，需要使用Selenium+ChromeDriver(或PhantomJS)
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#知乎
url = 'https://www.zhihu.com/question/45694301'

#知乎爬虫 https://blog.csdn.net/qq_28057541/article/details/61921632

#让界面滚动
def scroll(driver):
    driver.execute_script("""
           (function () {
               var y = document.body.scrollTop;
               var step = 100;
               window.scroll(0, y);


               function f() {
                   if (y < document.body.scrollHeight) {
                       y += step;
                       window.scroll(0, y);
                       setTimeout(f, 50);
                   }
                   else {
                       window.scroll(0, y);
                       document.title += "scroll-done";
                   }
               }
               setTimeout(f, 1000);
           })();
           """)
    
driver = webdriver.Chrome()
driver.get(url)
scroll(driver)

#等待滑到页面最下方
time.sleep(150)
html = driver.page_source

soup = BeautifulSoup(html,'lxml')
storys = soup.find_all('div',class_='List-item')
for story in storys:
    nameLabel = story.find('meta',itemprop='name')
    name = nameLabel["content"]
    with open('D:/thisme_D/Python/workspace/python_study_file/有哪些关于刀的故事/By '+str(name)+'.txt','w',encoding = 'utf-8') as f:
        storyText = story.find('span', class_="RichText ztext CopyrightRichText-richText")
        #输出方式一： 会打印全文 包括图片链接地址
        for string in  storyText.strings:
            f.write(repr(string) + '\n')        
        #方式一结束
        #输出方式二： 会有none出现
        #try:
        #   storyPages = storyText.find_all('p')
        #    for storyPage in storyPages:
        #        f.write(str(storyPage.string)+"\n")
        #        #输出方式二结束
        #    print('By '+str(name)+' has been finished')
        #except Exception:
        #    print(storyText)
        #    print('===Something is wrong on writing to txt')
            
print('That is all')