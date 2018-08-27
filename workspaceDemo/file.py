#coding=utf-8

import os

#文件读写

#获取用户输入 input()
x = input("input something:")
print(x)

#打开文件
file_open = open("F:/test.txt")
#文件路径
print(file_open.name)
#文件是否关闭状态 true or false
print(file_open.closed)
#打开文件的访问模式
print(file_open.mode)
#关闭文件
file_open.close()

#文件追加内容   a:访问模式，追加
file_append = open("F:/test.txt","a")
file_append.write("\n append.")
file_append.close()

#打开文件   r+:访问模式 打开读写文件。文件指针放在文件的开头。  encoding=“utf-8”文件编码格式
file_read = open("F:/test.txt","r+",encoding="utf-8")
#读取文件
str = file_read.read()
print(str)
#
file_read = open("F:/test.txt","r+",encoding="utf-8")
#指定字节长度10
str10 = file_read.read(10)
print(str10)
file_read.close()

#更改文件名称
os.rename("F:/test.txt","F:/test1.txt")

#删除指定文件
#os.remove("F:/test.txt")

#创建目录
os.mkdir("F:/test")

#使用当前目录
os.chdir("F:/test")
#获取当前目录
print(os.getcwd())

#删除指定目录
os.rmdir("F:/test")