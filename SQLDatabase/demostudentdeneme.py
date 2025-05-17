import mysql.connector
from datetime import datetime
from connection import connection

class Student:
    connection = connection
    mycursor = connection.cursor()

    
    def __init__(self, studentNumber, name, surname, birthdate, gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO student ( StudentNumber, name, Surname, Birthdate, Gender) VALUES ( %s, %s, %s, %s, %s)"
        value = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender)
        Student.mycursor.execute(sql, value)

        try:
        
            Student.connection.commit()
            print(Student.mycursor.rowcount, "records were inserted.")
        
        except mysql.connector.Error as err:
            print("hata : ", err)
        
        finally:
            Student.connection.close()
            print("database bağlantısı kapandı")  


    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO student ( StudentNumber, name, Surname, Birthdate, Gender) VALUES ( %s, %s, %s, %s, %s)"
        values = students
        Student.mycursor.executemany(sql, values)

        try:
        
            Student.connection.commit()
            print(Student.mycursor.rowcount, "records were inserted.")
        
        except mysql.connector.Error as err:
            print("hata : ", err)
        
        finally:
            Student.connection.close()
            print("database bağlantısı kapandı")  