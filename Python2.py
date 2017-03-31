# A Python program to demonstrate inheritance 
 

class Person(object):
     

    def __init__(self, name):
        self.name = name
 
 
    def getName(self):
        return self.name
 
    def isEmployee(self):
        return False
 
 

class Employee(Person):
 
    def isEmployee(self):
        return True
 

emp = Person("SAITEJA")  
print(emp.getName(), emp.isEmployee())
 
emp = Employee("DASARI") 
print(emp.getName(), emp.isEmployee())
