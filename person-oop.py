
from classtools import AttrDisplay





class Person:   #start a class
    #initializaition - Constructor takes three arguments, self is the new instance object
    def __init__(self, name, job =  None, pay : float = 0 ): #In OO terms, self is the newly created instance object, and name, job, and pay become state information—descriptive data saved on an object for later use.
        self.name = name
        self.job = job
        self.pay = pay
        

    def lname(self):
        return self.name.split()[-1]

    def fname(self):
        return self.name.split()[0]

    def giveRaise(self, percent):
        self.pay = self.pay * (1 + percent)

    def __repr__(self):
        return "Person: [{} {}, {:,.2f}]".format(self.fname(), self.lname(), self.pay)


class Manager(Person):

    #redefine constructor for subclass by running original with "Müdür"
    def __init__(self, name, pay):
        #super().__init__(name, pay)
        Person.__init__(self, name, "Manager", pay)
    




    #bad way
    # def giveRaise(self, percent, bonus = .10):
    #     self.pay = self.pay *(1 + percent + bonus)

    def giveRaise(self, percent, bonus = .10):   #instance.method(args..) translated to class.method(instance, args....)
        Person.giveRaise(self, percent + bonus)  #call Person's version of giveRaise()


  






# Aggregate embedded objects into a composite
class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def listAll(self):
        for person in self.members:
            print(person)



if __name__ == "__main__":
    #test kodu
    toygar = Person("Toygar Par")
    xxxxxxx = Person("Özdemir Par")
    besen = Person("Besen Par", job="Manager", pay = 45000)

    print(toygar.name, toygar.pay)
    print(besen.name, besen.pay)
    print(toygar.name.split()[-1])
    besen.giveRaise(.10)
    print(f"Besen {besen.lname()}'s pay is : {'{:,.2f}'.format(besen.pay)}")







    taco = Manager("Taco Par", 75000)    # __init__
    print("Previous Pay:" , taco.pay)
    taco.giveRaise(.25)                           #run customized version giveRaise()
    print(taco.lname(), ",", taco.fname())        #runs inherited methods
    print(taco)                                   #runs inherited __repr__



    print("ALL Persons:")

    for obj in (toygar, xxxxxxx, besen, taco):
        obj.giveRaise(.10)
        print(obj)