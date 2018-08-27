#coding=utf-8
# -*- coding:utf-8 -*-
#两种预设编码格式

#python变量类型

a=123
print(a)

num=100
flo=99.99
name="zhangsan"

print(num)
print(flo)
print(name)

print(num+flo)
print(flo-num)

a=b=c=1
print(a)
print(b)
print(c)

x,y,z=21,"name",110
print(x)
print(y)
print(z)
#String字符串
str = "hellopython"
print("str[0]="+str[0])
print("str[5:11]="+str[5:11])
print("str[2:]="+str[2:])
print("str[-1]="+str[-1])
print("str*2="+str*2)
print("str+!!!="+str+'!!!')

#列表list
list=[110,120,"jc","yy",11.9,'hj','mszh']
print('list = ',list)
print("list[0]=",list[0])
print("list[2:5]=",list[2:5])
print("list[2:]=",list[2:])
print("list[-1]=",list[-1])
print("list[-3:-1]=",list[-3:-1])

linkList=['link','jia',666]
print('list + linkList =',list+linkList)

#元组
tuple = ("tuple","nolist",110,120,'gg',"qq",666)
print("tuple = ",tuple)
print("tuple[0] = ",tuple[0])
print("tuple[2:5] = ",tuple[2:5])
print("tuple[2:] = ",tuple[2:])
print("tuple[-1] = ",tuple[-1])
print("tuple[-3:-1] = ",tuple[-3:-1])

linktuple = ("link","ddd")
print("tuple + linktuple = ",tuple+linktuple)

list[0] = 1111111
print("list = ",list)
#tuple[0] = "tuple111"    错误，元组不可以更新
#print("tuple = ",tuple)

#字典
dict = {}
dict[110] = {"警察"}
dict["火警"] = {119}
print("dict = ",dict)
print("dict['火警'] = ", dict["火警"])

tinydict = {'110':'抓小偷','火警':119}
print("tinydict = ",tinydict)
print("tinydict[110] = ",tinydict["110"])
print("tinydict.keys() = ",tinydict.keys())
print("tinydict.values() = ",tinydict.values())