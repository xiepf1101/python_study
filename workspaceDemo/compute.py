#coding=utf-8

#python 运算符

a = 10
b = 21
#计算运算符
print(a+b)
print(a-b)
print(a*b)
print(b/a)
print(b%a)
print(a**b)
print(b//a)

#关系运算符
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

#赋值运算符
c=a+b
print(c)
c += a
print(c)
c -= a
print(c)
c *= b
print(c)
c /= a
print(c)
c %= a
print(c)
c **= a
print(c)
c //= a
print(c)

#逻辑运算符
a = True
b = False
print(a and b)
print(a or b)
print(not(b))

a = "string"
b = "str"
print(b in a)
print(b not in a)

c = tuple(a)
print(c)
d = tuple(b)
print(d)
print(d in c)
print(d not in c)

#身份运算符
a = 20
b = 20
print(a is b)
print(a == b)
print(a is not b)

#if...else...
var = 11
if var == 11 : 
    print("ok")
    print("okk")
    
else : print("no")