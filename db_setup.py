import pymysql
import dbconfig

connection = pymysql.connect(host = 'mikekitckchan.mysql.pythonanywhere-services.com', user = mikekitckchan, passwd = Fong1029$)

try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS crimemap"
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS crimemap.crimes(
        id int NOT NULL AUTO_INCREMENT,
        latitude FLOAT(10, 6),
        longitude FLOAT(10, 6),
        date DATETIME,
        category VARCHAR (50),
        description VARCHAR (1000),
        updated_at timestamp,
        PRIMARY KEY(id)
        )"""
        cursor.execute(sql)
    connection.commit()
finally:
    connection.close()