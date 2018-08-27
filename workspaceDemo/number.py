#coding=utf-8
import math
import random

#数字
var1 = 1
var2 = 10
print(var1)
print(var2)
#del var1 删除对数字对象的引用

#int  无限大  （python2中有 long 类型）
int1 = 100
print(int1)

#float 浮点数
float1 = 0.012
print("float1",float1)
float2 = 2.5e2  #=2.5×10×10
print("float2",float2)

#complex 复数
complex1 = 3.14j
print(complex1)

#数字类型转换
x = 11.22
print(x) #float
x = int(x)  #转为int
print(x)
x = float(x)  #转为float
print(x)
#x = long(x)  #转为long类型 python2.0
#print(x)
x = complex(x) #转为complex复数
print(x)

#数字函数
x = -11
print(x)
x = abs(x)  #绝对值
print(x)
x = math.ceil(x) #返回不小于(大于等于)x的最小整数
print(x)
x = math.exp(x) #e的x次幂
print(x)
x = math.fabs(x)   #x的绝对值
print(x)
x = math.floor(x) #返回不大于(小于等于)x的最大整数
print(x)
x = math.log(x) #返回x的自然对数(x > 0)。
print(x)
x = math.log10(x) #返回10的x的对数
print(x)

x,y,z = 1,2,3
a = max(x,y,z)
print(a) #返回给定参数中的最大值
a = min(x,y,z)
print(a) #返回给定参数中的最小值
a = math.modf(x)    # 	将x的分数和整数部分切成两项放入元组中，两个部分与x具有相同的符号。整数部分作为浮点数返回。
print(a)
a = pow(y,z) #返回y的z次方
print(a)
a = round(-0.5333) #四舍五入
print(a)
a = math.sqrt(4) #平方根
print(a)

#随机数函数
str1 = "hello"
a = random.choice(str1) #来自列表，元组或字符串的随机项目。
print(a)
a = random.randrange(1,100,2) # 从范围(start, stop, step)中随机选择的元素。    start - 范围的起始点，这将包括在范围内，默认值为0。stop - 范围的起终点，这将包括在范围内，默认值为1。step - 跳跃值，不包括在范围内。
print(a)
a = int(random.random()*10+1) #返回随机浮点数r(0 <= r < 1)
print(a)
list = [1,2,3,4]
print("list",list)
random.shuffle(list) #将列表的内容位置随机打乱
print(list)
a = random.uniform(1,2) #返回随机浮点数 r (x <= r < y)
print(a)

#三角函数
a = math.acos(1) #返回x的弧余弦值
print(a)
a = math.asin(1) #返回x的弧线正弦
print(a)
a = math.atan(1) #返回x的反正切
print(a)
a = math.atan2(-1,1) #返回atan(y/x)
print(a)
a = math.cos(1) #返回x弧度的余弦
print(a)
a = math.hypot(0,2) #返回欧几里得规范
print(a)
a = math.sin(1) #返回x弧度的正弦
print(a)
a = math.tan(1) #返回x弧度的正切值
print(a)
a = math.degrees(1) #将角度x从弧度转为度
print(a)
a = math.radians(30)  #将角度转为弧度
print(a)





 
