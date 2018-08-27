#coding=utf-8

#日期与时间
import time
import datetime
#日历 calendar
import calendar


#当前时间
print(datetime.datetime.now())

#时间差
starttime = datetime.datetime.now()
#等待10s
time.sleep(1)
endtime = datetime.datetime.now()
#时间差 秒
print((endtime - starttime).seconds)

#计算十天后的时间
currentdate = datetime.datetime.now()
tendate = currentdate + datetime.timedelta(days = 10)
print(str(tendate))
print(tendate.ctime())

#获取两个时间的时间差
t = ( datetime.datetime(2018,11,8,12,0,0) - datetime.datetime.now() ).total_seconds()
print("t = ",t)

#时间间隔
ticks = time.time()
#当前时间与1970-01-01间隔多少秒
print("ticks = ",ticks)

#获取当前时间
print(time.localtime())
#格式化时间
curtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print("curtime = ",curtime)

#获取格式化时间
localtime = time.asctime(time.localtime())
print(localtime)

#日历 calendar
cal = calendar.month(2017,11)
print(cal)