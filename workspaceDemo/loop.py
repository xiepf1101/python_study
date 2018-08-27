#coding=utf-8
import sys

#循环
list = [1,2,3,4]
print(list)

it = iter(list)
#print("next = ",next(it))

for x in it : print(x)

#it = iter(list)
#while True:
    #try:
        #print("next = ",next(it))
    #except StopIteration:
        #print("没有东西可以输出了")
        #sys.exit()

print("break ： 终止循环语句转至执行循环外的后续操作")        

it = iter(list)
for y in it : 
    if y <= 3 : 
        print(y)
    else :
        print("break")
        break

print("success")

print("continue : 跳出本次循环执行下一次循环")

it = iter(list)
for y in it : 
    if y == 2 :
        print("contiune")
        continue
    else :
        print(y)

print("success")

print("pass : 在不需要执行的情况下 并要求保证语法")

it = iter(list)
for y in it : 
    if y == 2 :
        print("pass")
        pass
    else :
        print(y)

print("success")

def fibonacci(n): #generator function
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(5) #f is iterator object

while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()