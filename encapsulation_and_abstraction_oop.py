#Mechanism of hiding data implementation- Instance variables are kept private and there's only one accessor method from the outside with which we can access or change these instance variables
#Restict access to public methods called getter and setter methods .

class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #lets's say salary should be private except probably the HR department to get and set the salary. We create an internal attribure
        self._salary = None
        self._num_bugs_solved = 0
        #If we want to make it really private we can use a double leading underscore __#

    def code(self):
        self._num_bugs_solved += 1
#getter
    def get_salary(self):
        return self._salary
    
#setter
    def set_salary(self, base_value):
        self.salary = self._calculate_salary(base_value)
        #Check value and enforce constraints
        # if value < 1000:
        #     self._salary = 1000
        # if value > 20000:
        #     self._salary = 20000
        # self._salary = value

    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self.num_bugs_solved <100:
            return base_value * 2
        return base_value * 3


se = SoftwareEngineer("Max", 25)
se.set_salary(6000)
print(se.get_salary())



se2 = SoftwareEngineer("Maxi", 25)
print(se.age, se.name, se._salary)

for i in range(70):
    se.code()

        
print(se._num_bugs_solved)