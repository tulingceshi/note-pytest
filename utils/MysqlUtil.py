#1、导入pymysql包
import pymysql
#2、连接database
#3、获取执行sql的光标对象
#4、执行sql
#5、关闭对象


#1、创建封装类
class Mysql:
    def __init__(self,host,user,password,database,port):
        # 2、初始化数据，连接数据库，光标对象
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        self.cursor = self.conn.cursor()
    #3、创建查询、执行方法

#4、关闭对象
conn = pymysql.connect(host="localhost",user="root",password="root",database="liuzhimin",port=3306)
# 3、获取执行sql的光标对象
cursor = conn.cursor()
# 4、执行sql
sql = "select u_name,age from students"
cursor.execute(sql)
res = cursor.fetchone()
print(res)
# 5、关闭对象
cursor.close()
conn.close()
