import mysql.connector
from datetime import datetime
from connection import connection

class Student:
    connection = connection
    mycursor = connection.cursor()

    
    def __init__(self, id,studentNumber, name, surname, birthdate, gender):
        if id is None:
            self.id = 0

        else:
            self.id = id
            
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    # def saveStudent(self):
    #     sql = "INSERT INTO student ( StudentNumber, name, Surname, Birthdate, Gender) VALUES ( %s, %s, %s, %s, %s)"
    #     value = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender)
    #     Student.mycursor.execute(sql, value)

    #     try:
        
    #         Student.connection.commit()
    #         print(Student.mycursor.rowcount, "records were inserted.")
        
    #     except mysql.connector.Error as err:
    #         print("hata : ", err)
        
        

    
        
        


    # @staticmethod
    # def saveStudents(students):
    #     sql = "INSERT INTO student ( StudentNumber, name, Surname, Birthdate, Gender) VALUES ( %s, %s, %s, %s, %s)"
    #     values = students
    #     Student.mycursor.executemany(sql, values)

    #     try:
        
    #         Student.connection.commit()
    #         print(Student.mycursor.rowcount, "records were inserted.")
        
    #     except mysql.connector.Error as err:
    #         print("hata : ", err)
        
        

    # @staticmethod 
    # def studentInfo():
    #     sql = "select * from student;"

    #     Student.mycursor.execute(sql)



    @staticmethod
    def getStudentById(id):
        sql = "select * from student where id =  %s;"
        val = (id,)

        Student.mycursor.execute(sql, val)
            

        
              
        try: 
            
            result = Student.mycursor.fetchall()
                       
            print(result)
            print("*****************")
            
            for student in result:
                print(student)

            print("*****************")

            for student in result:
                print(student[1]) #sadece öğrenci numaraları

            print("*****************")

            for student in result:
                print(f"name: {student[2]}  surname : {student[3]}")
                

            
            
            
        
        except mysql.connector.Error as err:
            print("hata : ", err)
        
        
        
        
    def updateStudent(self):
        sql = " update student set studentnumber= %s, name = %s, surname =%s, birtdate =%s, gender =%s where id =%s;"
        vals = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender, self.id)

        Student.mycursor.execute(sql, vals)

        try:
        
            Student.connection.commit()
            print(Student.mycursor.rowcount, "records were updated.")
        
        except mysql.connector.Error as err:
            print("hata : ", err)        
            



student = Student.getStudentById(7)


#student = Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])

student.name = "Çınar"
student.surname = "Turan"

student.updateStudent()
