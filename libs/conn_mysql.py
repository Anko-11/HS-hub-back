import pymysql
from config.settings import DATABASE_HOST,DATABASE_PORT,DATABASE_USER,DATABASE_SCHEM,DATABASE_PASSWD


def conn_mysql():
    conn = pymysql.connect(
        host=DATABASE_HOST,
        user=DATABASE_USER,
        port=DATABASE_PORT,
        password=DATABASE_PASSWD,
        db=DATABASE_SCHEM
    )
    return conn
