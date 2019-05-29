#This program creates a text file with names, e-mails and numbers
#The text file is randomly generated, so each time the full name will be different, the phone numbers will be different etc.

import random as r
from itertools import permutations

class Person:

    def __init__(self, list_names, list_surnames):
        self.list_names = list_names
        self.list_surnames = list_surnames
        self.name = "name"
        self.surname = "surname"
        self.fullname = "fullname"
        self.phone = 0
        self.email = "email"
        self.numbers = [0,1,2,3,4,5,6,7,8,9]
    
    def create_names(self):
        r1 = r.randint(0, len(self.list_names)-1)
        r2 = r.randint(0, len(self.list_surnames)-1)
        
        self.name = self.list_names[r1]
        self.surname = self.list_surnames[r2]
        self.fullname = "{} {}".format(self.name, self.surname)
        self.email = "{}.{}@bogusmail.com".format(self.name, self.surname)

        
    
    def create_phone_number(self):
        self.first_phone_part = r.sample(self.numbers, 3)
        self.second_phone_part = r.sample(self.numbers, 3)
        self.third_phone_part = r.sample(self.numbers, 3)

        #The next line of code is ugly and I bet it can be written better
        self.phone = "{}{}{}-{}{}{}-{}{}{}".format(self.first_phone_part[0], self.first_phone_part[1], self.first_phone_part[2],
                                                    self.second_phone_part[0],self.second_phone_part[1],self.second_phone_part[2],
                                                    self.third_phone_part[0],self.third_phone_part[1],self.third_phone_part[2])


    def save(self):
        with open("randnames.txt", "a") as f:
            f.write(self.fullname + "\n")
            f.write(self.email + "\n")
            f.write(self.phone + "\n")
            f.write("\n")



names = [
"Bob",
"Marina",
"Hans",
"Elaine",
"John",
"Josh",
"Sam",
"Ezekiel",
"Kilian",
"Jessica",
"Charles",
"Carl",
"Florence",
"Evariste",
"Otto",
"Harper",
"Fjodor"]

surnames = [
"Muller",
"Schafer",
"Augustine",
"Hunter",
"Miner",
"Glob",
"Pope",
"Williamson",
"Mariane",
"Simpson",
"Berners",
"Galois",
"Kronecker",
"Blake",
"Boyle",
"Lee",
"Dostojewski"]


x = Person(names, surnames)
for i in range(101):
    x.create_names()
    x.create_phone_number()
    x.save()