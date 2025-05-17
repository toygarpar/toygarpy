import mysql.connector
from datetime import datetime
from connection import connection
from student import Student
from teacher import Teacher
from klass import Class
from lesson import Lesson



class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self, id):
        sql ="select * from student where id=%s;"
        val = (id,)
        self.cursor.execute(sql, val)
        try:
            obj = self.cursor.fetchone()
            print(obj)
            #return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6])  #bunun yerine studentsda class oluşturduk
            return Student.createStudent(obj)

        except mysql.connector.Error as err:
            print("Error")
            
    def deleteStudent(self, studentid):
        sql = "delete from student where id=%s"
        value = (studentid,)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt silindi/deleted.')
        except mysql.connector.Error as err:
            print('hata:', err)
        
            
    
    def getClasses(self):
        sql ="select * from class;"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            
            print(obj)
            print("*********")
            return Class.CreateClass(obj)
            #return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6])

        except mysql.connector.Error as err:
            print("Error")
        

    def getStudentByClassId(self, classid):
        sql ="select * from student where classid=%s;"
        vals = (classid,)
        self.cursor.execute(sql, vals)
        try:
            obj = self.cursor.fetchall()
            print(obj)
            print("*********")
            return Student.createStudent(obj)
            #return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6])

        except mysql.connector.Error as err:
            print("Error")
        
    def addOrEditStudent(self, student: Student):
        pass

    
    def addStudent(self, student : Student):
        sql = "INSERT INTO Student(studentNumber,Name,Surname,Birthdate,Gender,classid) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber,student.name, student.surname,student.birthdate,student.gender, student.classid)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata:', err)
        #connectionı kapatmayacağız sonrasın güncelleme yapacağız

    def editStudent(self, student : Student):
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s, classid=%s where id=%s"
        value = (student.studentNumber,student.name, student.surname,student.birthdate,student.gender, student.classid, student.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi.')
        except mysql.connector.Error as err:
            print('hata:', err) 

    def addTeacher(self, teacher : Teacher):
        pass

    def editTeacher(self, teacher : Teacher):
        pass

    #def __del__(self):   #manually close connection in notebook
        #self.cursor.close()
        #self.connection.close()
        #print("Cursor ve Connection Closed!")