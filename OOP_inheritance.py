
#Inherit,Extend, Override

class Employee: #Use it as a base class
#storing some attributes
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working...")

    def debug(self):
        print(f"{self.name} is debugging...")


class SoftwareEngineer(Employee): #child class that inherits the parents class.We use parenthesis.Inherits all functions from employees
    def __init__(self, name, age, salary, level): # Inherits all the fucntions
    #We do not do the sel.name process we just call the initializer
      super().__init__(name, age, salary)
      #to store other parameters
      self.level = level

    def debug(self):
        print(f"{self.name} is coding...")



class Designer(Employee):
    def draw(self):
        print(f"{self.name} is drawing...")



#lets create the instances
se = SoftwareEngineer(f"Colby", 24, 7000, "Junior") 
print(se.name, se.age, se.salary, se.level) #Colby 24
se.work() #Colby is working...
se.debug() #Colby is debugging...

d = Designer("Lorin", 38, 7000)
print(d.name, d.age) #Colby 24
d.work() #Lorin is working...
d.draw() #Lorin is drawing


#? Polymorphism-Many shapes-Will work in any super class and any sub-class as well
#Gives a way to use classes as its parents and keep it as they are
def motivate_employees(employees):
    for employee in employees:
        employee.work()


motivate_employees(Employees)