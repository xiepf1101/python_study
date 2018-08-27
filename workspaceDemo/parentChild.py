#coding=utf-8

#类的继承
class Parent:
    
    parentAttr = 100
    
    def __init__(self):
        print("i am parent")
        
    def parentMethod(self):
        print("parent method")
        
    def myMethod(self):
        print("parentMethod")
        
    def setAttr(self,attr):
        Parent.parentAttr = attr
    def getAttr(self):
        print("parentAttr:",Parent.parentAttr)
    
#继承 className(ParentClassName1,ParentClassName2,...) 
class Child(Parent):
    def __init__(self):
        print("i am child")
    
    def childMethod(self):
        print("child method")
    
    def myMethod(self):
        print("childMethod")
    
c = Child()
c.childMethod()
#父类方法
c.parentMethod()
c.setAttr(123)
c.getAttr()

#重载父类myMethod方法
c.myMethod()

#issubclass(sub,sup) 判断sub类和sup类间的关系  sub继承sup则返回True
print(issubclass(Child,Parent))

