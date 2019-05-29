#An Employee class

class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    #Getter function just like in Java
    @property
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)
    
    #Setter function for self.first and self.last
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

emp1 = Employee("John", "Wick")
name = "Winston Churchill"

emp1.fullname = name
print(emp1.fullname)
print(emp1.first)
print(emp1.last)
print(emp1.fullname)
del emp1.fullname
print(emp1.first)