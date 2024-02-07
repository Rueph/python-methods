#should have position, name, age,level and salary
#Use a list
se1 = ["Software Engineer", "Max", 20, "Junior", 5000]
se2 = ["Sofware Engineer", "Lisa", 25, "Senior", 7000]
#Can be cumbersome and error prone for example what happens when the name is missing or something differrent, or when something changes..
#Lists are not perfect for such kind of data representation. That's why we use classes. They contain functions that determine the behaviour of our class.
#Class is a blueprint of how something should be defined.

#It starts with the keyward class and the name of the class
#Incase theres a designer 
d1 = ["Designer", "Phillip"] #Calling this from a global function will print Phillip as a software engineer...Better to write it in the class

class SoftwareEngineer:
    #Class attribute- This can be used on the whole class because it is the same attribute for each instance

    alias = "Keybard Magician"
    
     # Special method to initialize our object
    def __init__(self, name, age, level, salary):
        #Instance attributes
        self.name = name #name is tied to a specific instance cannot be used for the whole class
        self.age = age
        self.level = level
        self.salary = salary

#instance method
#Functions in classed 
    def code(self):
        print(f"{self.name} is writing code...")
        #Recap
#Create a class - It is the blue print
#Create instance or object e.g this is an instance: se1 = SoftwareEngineer("Max", 20, "Junior", 5000)
#Difference between a class and instance
#Instance attributes are defined like : def __init__(self)


    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}...")


    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}...")
    
    #Returning functions

    def information(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information
    
#1. dunder method
    #Double underscore methods are special and start with double leading and trailing underscore
    #Another method is string method
    def __str__(self):#string method - Will be executed wherever our object is converted to a string
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information
    
    #Equal method
    def __eq__(self, other): #Compare two objects
        return self.name == other.name and self.age == other.age
    #You almost will never see below kind f function, normaly use a decorator method to prevent it from crashing when we call it by its instance e.g se2.entry_salary(24)
    #These are not ties to the instance attriutes for example self.self will produce an error. You an use it on both the class e.g SoftwareEngineer or instance e.g se2 but you cannot use it to acess the self attributes
    @staticmethod #decorator
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000






    #create an instance of this class
se1 = SoftwareEngineer("Max", 20, "Junior", 5000)
se2 = SoftwareEngineer("Lisa", 25, "Senior", 7000)
se3 = SoftwareEngineer("Lisa", 25, "Senior", 7000)

#Accessing the attributes
print(se1.name, se1.age)

#Recap
#Create a class - It is the blue print
#Create instance or object e.g this is an instance: se1 = SoftwareEngineer("Max", 20, "Junior", 5000)
#Difference between a class and instance
#Instance attributes are defined like : def __init__(self)


   
  


#Double underscore methods are special and start with double leading and trailing underscore
#Another method is string method
# def __str__(self):#string method - Will be executed wherever our object is converted to a string
#     information = f"name = {self.name}, age = {self.age}, level = {self.level}"
#     return information


   



se1.code() #Max is writing code
#Returning functions



se2.code() #Lisa is writing code
se1.code_in_language("Python") #Max is writing code in Python
se2.code_in_language("C#") #Lisa is writing ode in C#
print(se1.information())#name = Max, age = 20, level = Junior
print(se1)#name = Max, age = 20, level = Junior
print(se2) #name = Lisa, age = 25, level = Senior
print(se2 == se3)#true
print(SoftwareEngineer.entry_salary(24)) #5000



