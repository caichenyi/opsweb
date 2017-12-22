import pymysql

db_name = 'test01'
db_host = '192.168.6.15'
db_port = 3306
username = 'root'
password = 'iscs@2016up'


db = pymysql.connect(host=db_host, user=username, passwd=password, port=db_port, db=db_name)
# cursor = db.cursor()
# sql = """insert into test02 values(2, 'zhang');"""
# cursor.execute(sql)
# db.commit()
db.close()