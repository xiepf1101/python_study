#coding=utf-8
#函数

#函数块以关键字def开头，后跟函数名和小括号(())。
#任何输入参数或参数应放置在这些小括号中。也可以在这些小括号内定义参数。
#每个函数中的代码块以冒号(:)开始，并缩进。
#函数内的第一个语句可以是可选语句 - 函数的文档或docstring字符串。
#语句return [expression]用于退出一个函数，可选地将一个表达式传回给调用者。如果没有使用参数的return语句，则它与return None相同。

def printFunction(str):
    "字符串输出函数"   #函数内的第一句（可选语句）
    print("str:",str)
    return None    

#函数调用
printFunction("printFunction")

#参数引用与传递
#Python语言中的所有参数(参数)都将通过引用传递。如果在函数中更改参数所指的内容，则更改也会反映在调用函数的外部
def changeme(mylist):
    mylist[0] = 100
    return 

mylist = [1,2,3]
changeme(mylist)
print("mylist : ",mylist)


#参数mylist是changeme1()函数的局部变量。在函数中更改mylist不影响mylist的值。函数执行完成后
def changeme1(mylist):
    mylist = [100,200,300]
    return 

mylist = [1,2,3]
changeme1(mylist)
print("mylist : ",mylist)

#函数参数
#1.必需参数
def print_(str):
    print(str)
    return 
print_("必须参数")

#2.关键词参数
def print1(name,age):
    print("name : ",name,"age : ",age)
    return 
#调用函数是传参可无序，但需要将关键词和参数进行匹配
print1(age = 15,name = "张三")

#3.默认参数
def print2(name,age = 25):
    print("name : ",name,"age : ",age)
    return

print2("李四",17)
print2("王五")

#4.可变长度参数
def change_(arg1,*vartuple):
    print("arg1 : ",arg1)
    for var in vartuple:
        print("vart : ",var)
    return

change_(1)
change_(1,2,3)


#5.匿名函数  lambda函数
sum = lambda arg1,arg2 : arg1+arg2

print(sum(1,2))

#全局变量和局部变量
total = 100 #全局变量
def sum_():
    total = 2+3 #局部变量
    print(total)
    return 

sum_()
print("total : ",total)