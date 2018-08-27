#coding=utf-8

#操作mysql数据库

import pymysql

#  mysql version
#打开数据库连接
#db = pymysql.connect("127.0.0.1","root","root")
#创建游标 
#cursor = db.cursor()
#创建游标后   通过execute() 方法来执行sql语句  进行数据库的操作
#cursor.execute("SELECT VERSION()")  #查询mysql的版本号
#使用fetchone()方法获取单挑数据
#date = cursor.fetchone()
#打印
#print("datebase version:",date)
#关闭数据库连接
#db.close()

#  删除/创建 表
db = pymysql.connect("127.0.0.1","root","root","mysql") #ip username password datebaseName
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS employee") #如果table存在则删除
sql = """CREATE TABLE `employee` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `first_name` char(20) NOT NULL,
  `last_name` char(20) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `sex` char(1) DEFAULT NULL,
  `income` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
cursor.execute(sql)
print("create table successful")
db.close()

#增加数据
db = pymysql.connect("127.0.0.1","root","root","mysql")
cursor = db.cursor()
sql = """INSERT INTO EMPLOYEE (FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) VALUES ('Li','Si',19,'M',95)"""
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
    
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
       LAST_NAME, AGE, SEX, INCOME)
       VALUES ('Kobe', 'Bryant', 40, 'M', 8000)"""
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Max', 'Su', 25, 'F', 2800)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()


db.close()
print(sql)
print("insert successful")

# 查询数据
db = pymysql.connect("127.0.0.1","root","root","mysql")
cursor = db.cursor()
cursor.execute("SELECT * FROM employee")
date = cursor.fetchall()
print("date :",date)
db.close()

#查询表中数据 按照字典形式返回
db = pymysql.connect("127.0.0.1","root","root","mysql")
cursor = db.cursor()
sql = "SELECT * FROM EMPLOYEE \
    WHERE INCOME <= %d" % (1000)
try:
    cursor.execute(sql)
    resultAll = cursor.fetchall()
    for row in resultAll:
        #print(row)
        first_name = row[1]
        last_name = row[2]
        age = row[3]
        sex = row[4]
        income = row[5]
        print("name = %s %s,age = %s,sex = %s,income = %s" % \
              (first_name,last_name,age,sex,income))
except:
    import traceback
    traceback.print_exc()  #打印异常数据
    print("没有查询到数据")
    
db.close()


#更新 update
db = pymysql.connect("localhost","root","root","mysql")
cursor = db.cursor(pymysql.cursors.DictCursor)
cursor = db.cursor()
sql = "UPDATE EMPLOYEE SET AGE = AGE + 100 WHERE SEX = '%c'" % ('M')
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
    
db.close()

#删除 delete
db = pymysql.connect("localhost","root","root","mysql")
cursor = db.cursor()
sql = "DELETE FROM EMPLOYEE WHERE AGE < '%d'" % (40)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()