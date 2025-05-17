import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "toygarpar",
    password = "xxxxxxx",
    database = "shopdb"
)


cursor = db.cursor()



#örnek database oluştur
#cursor.execute("CREATE DATABASE exampledb")

#cursor.execute("SHOW DATABASES")

cursor.execute("CREATE TABLE categories (Id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")

cursor.execute("SHOW TABLES")

for i in cursor:

    print(i)



