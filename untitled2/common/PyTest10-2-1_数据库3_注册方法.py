import pymysql
# 3:45:30  第2-2课
"""
    111
"""

class Mysql_Login :
    def __init__(self,
                 database = 'merchandise',
                 host ='localhost',  # 本地数据库
                 user = 'root',
                 passwd = '123456',
                 port = 3306,
                 charset = 'utf8',
                 table =''):
        self.database = database
        self.host = host
        self.user = user
        self.passwd = passwd
        self.table = table
        self.charset = charset
        self.port = port
        self.connect_db()

    def connect_db(self):
        self.db = pymysql.connect(host=self.host,
                                  user=self.user,
                                  database=self.database,
                                  passwd=self.passwd,
                                  charset=self.charset,
                                  port = self.port)
        self.cur = self.db.cursor()

    def close_db(self):
        self.cur.close()
        self.db.close()

