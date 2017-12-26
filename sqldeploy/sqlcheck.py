from . import models

import pymysql

def mysql_connect(db_host, username, password, db_port, db_name):
    try:
        db = pymysql.connect(host=db_host, user=username, passwd=password, port=db_port, db=db_name)
        return True
    except:
        return False


def sql_selfreview(dbenv, content):
    # dbenv = models.DbEnv.objects.get(db_env=db_env)
    sql = content
    db = pymysql.connect(host=dbenv.db_host, user=dbenv.username, passwd=dbenv.password, port=dbenv.db_port, db=dbenv.db_name)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        cursor.close()
        db.close()
        return True
    except:
        cursor.close()
        db.close()
        return False


def sql_deploy(dbenv, content):
    sql = content
    db = pymysql.connect(host=dbenv.db_host, user=dbenv.username, passwd=dbenv.password, port=dbenv.db_port, db=dbenv.db_name)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        cursor.close()
        db.commit()
        db.close()
        return True
    except:
        cursor.close()
        db.close()
        return False