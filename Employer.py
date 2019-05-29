#Basic classes
#This class displays a message for each employee and some other information which can be accessed through the class

class Employee:

    num_of_employees = 0
    def __init__(self, firstName, lastName, workHours, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.workHours = workHours
        self.pay = pay

        Employee.num_of_employees += 1

    def fullname(self):
        return "{} {}".format(self.firstName, self.lastName)
    
    def message(self):
        print("This is " + self.fullname() + ". He/She worked {} hours this week and his/her pay is {} per hour.".format(self.workHours, self.pay))

    #Class methods take the instance of class, not of self. They can be seen as alternative constructors
    @classmethod
    def emp_with_hyphen(cls, emp):
        firstName, lastName, workHours, pay = emp.split("-")
        return cls(firstName, lastName, workHours, pay)

    #staticmethods are methods that neither take in self nor cls, meaning they don't know anything about the class
    @staticmethod
    def from_gender(g):
        if(g == 0):
            return "Female"
        else:
            return "Male"

class Developer(Employee):
    
    def __init__(self, firstName, lastName, workHours, pay, progLang):
        #Super is more maintainable for single inheritance than Employee.__init__(self, ...)
        super().__init__(firstName, lastName, workHours, pay)
        self.progLang = progLang
    

    def message(self):
        return print(self.progLang)
        

class Manager(Employee):
    
    def __init__(self, firstName, lastName, workHours, pay, emps = None):
        super().__init__(firstName, lastName, workHours, pay)
        if emps is None:
            self.emps = []
        else:
            self.emps = emps
    
    def add_emps(self, emps):
        if emps not in self.emps:
            self.emps.append(emps)
    
    def rem_emps(self, emps):
        if emps in self.emps:
            self.emps.remove(emps)
    
    def print_emps(self):
        for e in self.emps:
            print("-->" + e.fullname())

def main():
    emp1 = Employee("Bob", "Turner", 40 , 12.30)
    emp2 = Employee("Chloe", "Hunter", 35, 11.00)

    print(emp1.fullname())
    emp1.message()
    emp2.message()

    print(emp1.num_of_employees)
    print(emp2.num_of_employees)
    print(Employee.num_of_employees)

    emp3 = "Miranda-Mirandina-50-17.30"
    emp3_normalised = Employee.emp_with_hyphen(emp3)
    emp3_normalised.message()
    a = Employee.from_gender(1)
    print(a)

    dev1 = Developer("Bob", "Turner", 40 , 12.30, "C++")
    dev2 = Developer("Frank", "Johnson", 40 , 12.30, "Java")

    dev1.message()

    mgr_1 = Manager("Susana", "Susanita", 10, 100000, [dev1, dev2])
    print(mgr_1.fullname())
    mgr_1.print_emps()
    mgr_1.rem_emps(dev1)
    mgr_1.print_emps()


if __name__ == "__main__":
    main()