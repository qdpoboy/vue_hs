# -*- coding:utf-8 -*-
import MySQLdb
class MyDB:
    conn = None
    cur  = None

    #构造函数
    def __init__(self):
        self.conn = MySQLdb.connect(host="localhost",user="root",passwd="",port=3306,db="hs",charset="utf8")
        self.cur = self.conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        #这种方式查询返回的值默认的只能通过v[0]数字key来访问，想要通过表字段名来查询，需要加上self.conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        print 'xx'

    #析构函数
    def __del__(self):
        print 'yy'
        self.conn.commit()#提交  为什么之前的不用提交呢？跟数据库的引擎有关？回头测试一下
        self.cur.close()
        self.conn.close()
   
    #插入单条数据
    def insertData(self,sql):
        return self.cur.execute(sql)
   
    #插入一条数据
    def insertOne(self,sql,value):
        return self.cur.execute(sql,value)

    #插入多条数据
    def insertMany(self,sql,values):
        return self.cur.executemany(sql,values)

    #查询一条
    def getOne(self,sql):
        count = self.cur.execute(sql)
        return self.cur.fetchone()

    #查询多条
    def getMany(self,sql):
        count = self.cur.execute(sql)
        return self.cur.fetchall()

    #更新
    def updateData(self,sql):
        return self.cur.execute(sql)

    #特殊字符串转义
    def escape_string(self,val):
        return MySQLdb.escape_string(val)