#coding=utf-8

#正则表达式 re

import re

#re.match(regex,string,flags=0)    从句头开始匹配
#re.search(regex,string,flags=0)    检查字符串中任何位置的匹配

class regexDemo:
    
    regex = r"\w"   # r 声明正则表达式(应该是吧)   可省略
    
    def regexMethod(self,string):
        reMatch = re.match(self.regex,string,flags=0)  #匹配不成功返回None  成功返回匹配对象    
        print(reMatch.group())
        
reg = regexDemo()
reg.regexMethod("1")
        
line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
    print ("matchObj.group() : ", matchObj.group())
    print ("matchObj.group(1) : ", matchObj.group(1))
    print ("matchObj.group(2) : ", matchObj.group(2))
else:
    print ("No match!!")        

#search  检查字符串中任何位置的匹配
searchObj = re.search( r'Dogs', line, re.M|re.I)    #re.I 不区分大小写
   
if searchObj:
    print("searchObj.group() : ",searchObj.group())
else:
    print("no search")
    
#re.sub(pattern, repl, string, max=0)   根据正则表达式对原有字符串修改（截取）
phone = "2018-959-559 # This is Phone Number"
sub1 = re.sub(r"\D","",phone)
print("sub1 : ",sub1)
sub2 = re.sub(r"#.*$","",phone)
print("sub2 : ",sub2)

#http://www.yiibai.com/python/python_reg_expressions.html
