#coding=utf-8

#声明class
class Employee:
    
    empCount = 0    #类变量 其值在此类中的所有实例之间共享。 这可以从类或类之外的Employee.empCount访问
    
    #初始实例化方法   每个方法的第一个参数为self（调用方法是不需要传参）
    def __init__(self,name,salary):
        self.name = name    #赋值
        self.salary = salary
        Employee.empCount += 1
        
        
    def dispalyEmpCount(self):
        print(Employee.empCount)
        
    def dispalyEmp(self):
        #异常处理
        try:
            print ("name:",self.name,"salary:",self.salary)
        except Exception:
            print ("name:",self.name,"salary:","未透露")
        
#实例化   相当于构造函数        
emp1 = Employee("Maxsu", 2000)
#调用class中的方法
emp1.dispalyEmp()   

emp2 = Employee("张三",3000)
#修改属性值
emp2.salary = 2300
emp2.name = "lisi"
emp2.dispalyEmp()
#删除属性
del emp2.salary
emp2.dispalyEmp()
emp2.dispalyEmpCount()

Employee.empCount = 20
emp2.dispalyEmpCount()

#检查属性是否存在
print("is exists:",hasattr(emp2,"salary"))
#返回name属性的值
print("name:",getattr(emp2,"name"))
#给salary属性赋值
setattr(emp2,"salary",5666)
emp2.dispalyEmp()
#删除属性salary值
delattr(emp2,"salary")
emp2.dispalyEmp()

#包含该类的命名空间的字典
print("dict",Employee.__dict__)
#类文档字符串或无
print("doc:",Employee.__doc__)
#类名
print("name:",Employee.__name__)
#定义类的模块名称。此属性在交互模式下的值为“main”
print("module:",Employee.__module__)
#一个包含基类的空元组，按照它们在基类列表中出现的顺序
print("bases:",Employee.__bases__)

