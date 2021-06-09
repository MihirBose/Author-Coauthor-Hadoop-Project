import mysql.connector

def get_db_conn():
    conn=mysql.connector.connect(host="127.0.0.1",
        user="root",
        password="pwd",
        database="employees",
        auth_plugin='pwd')
    return conn