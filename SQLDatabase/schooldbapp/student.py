class Student:
       
    def __init__(self, id, studentNumber, name, surname, birthdate, gender, classid):
        if id is None:
            self.id = 0

        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.classid = classid

    @staticmethod
    def createStudent(obj):
        list=[]

        if isinstance(obj, tuple):  #eğer bir tuple geri geliyorsa
            list.append(Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6]))

        else: #eğer bir liste geri geliyorsa
            for i in obj:
                list.append(Student(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
                # list(i)
                # k=[]
                # for j in i:
                #     k.append(i[j])

                # tuple(k)
                # list.append(Student(k[0],k[1],k[2],k[3],k[4],k[5],k[6]))
                    

        return list
                