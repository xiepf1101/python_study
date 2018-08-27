#coding=utf-8

#重载运算符     数据隐藏
class Vector():
    
    #在secretCount 前+__则   __secretCount被隐藏
    __secretCount = 0
    
    def count(self):
        self.__secretCount+=1
        print(self.__secretCount)
    
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def __str__(self):
        return "Vector(%d,%d)" % (self.a,self.b)
    
    def __add__(self,other):
        return Vector(self.a + other.a,self.b + other.b)
    
v1 = Vector(2,10)
v2 = Vector(3,-1)
print(v1 + v2)

#数据隐藏
v3 = Vector(1,2)
v3.count()
v3.count()
#__secretCount 属性被隐藏   引用会报错
#print(v3.__secretCount)