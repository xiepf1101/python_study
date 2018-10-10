#coding=utf-8
#python3.7  操作 mysql

#导入操作mysql的模块
import pymysql as driver

#打开数据库连接    
db = driver.connect("localhost", "root", "root", "learn")

#使用cursor() 方法创建一个游标对象cursor
cursor = db.cursor()

#使用execute() 方法执行sql语句
cursor.execute("SELECT VERSION()")

#使用fetchone() 方法获取单条数据
data = cursor.fetchone()

print("Database version : %s "% data)

#关闭数据库连接
db.close()

#----更新表格操作

db = driver.connect("localhost", "root", "root", "learn")

cursor = db.cursor()

sql = "DROP TABLE IF EXISTS EMPLOYEE"

cursor.execute(sql)

sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

db.close()

#----新增操作

db = driver.connect("localhost", "root", "root", "learn")

cursor = db.cursor()

sql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Mac', 'Mohan', 20, 'M', 2000) "

try:
    cursor.execute(sql)
    #提交到数据库执行
    db.commit()
except:
    #发生异常   回滚
    db.rollback()
    
db.close()

#----新增操作

# 打开数据库连接
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
                                               ('Mac', 'Mohan', 20, 'M', 2000)
try:
    # 执行sql语句
    cursor.execute(sql)
    # 执行sql语句
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()

#----查询操作

# 打开数据库连接
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
            # 打印结果
        print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income ))
except:
    print ("Error: unable to fetch data")

# 关闭数据库连接
db.close()

#----更新操作

# 打开数据库连接
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()

#----删除操作

# 打开数据库连接
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭连接
db.close()