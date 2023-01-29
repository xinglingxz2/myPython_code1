import pymysql
#  数据库操作2  库内保存图片
#

# 创建连接
db = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='stu')
cur = db.cursor()  #获取游标

# # 获取文件
# with open('hai1.jpg','rb') as fd:  # rb方式打开
#     data = fd.read()
#
# # 写入到数据库
# try:
#     sql = "insert into Images values (1,'hai1.jpg',%s)"
#     cur.execute(sql,[data])
#     db.commit()
# except Exception as e:
#     db.rollback()   # 回滚
#     print(e)

sql2 = "select * from Images where filename ='hai1.jpg';"
cur.execute(sql2)
image = cur.fetchone()  # 输出结果 为 元组类型
with open(image[1],'wb') as fd:  #保存文件的名称为 image元组的1
    fd.write(image[2])  #写入为image元组的2内容

cur.close()
db.close()

