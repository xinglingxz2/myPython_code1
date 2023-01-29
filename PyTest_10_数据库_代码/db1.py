import pymysql
#  数据库操作1
#

# 创建连接
db = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='stu')
cur = db.cursor()  #获取游标

for x in range(1):
    id = int(input(" id :"))
    name = input("name ：")
    age = int(input("age = :"))

    # SQL命令语句
    # sql ="insert into stu (id,name,age) values (%d,'%s',%d);"%(id,name,age)  #方法1
    # sql ="insert into stu (id,name,age) values (%s,%s,%s);"  #方法2
    sql ="update stu set name=('小桂子') where name ='黑土';"
    try:
        #cur.execute(sql)  # 3.执行命令   #方法1
        cur.execute(sql)  #方法2
        db.commit () #5.提交
    except Exception as e:
        db.rollback () #6.失败 回滚命令（之前状态）
        print("Faild:",e)
    # result = cur.fetchmany(3)
    result = cur.fetchall() #查询结果

#==========================================

#exe = cur.execute(sql)  # 执行命令，返回查询的条数 成功返回值为1
#result = cur.fetchone()
#result = cur.fetchmany(3)
#result = cur.fetchall() #查询结果

# print(result) #显示出
# db.commit() #链接提交，用于对数据库的增删改

cur.close() #关闭游标  # 关闭部分
db.close() #关闭链接
