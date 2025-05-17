import mysql.connector
import mysqlx

mydb = mysql.connector.connect(
    host = "localhost", #192.23.48.45
    user = "root",
    password = "xxxxxxx"



)
print(mydb)