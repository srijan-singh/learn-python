"""WAP to increment the employee
salaries on the basis of their
designation. Use employee name,
id, designation and salary as data
member and inc_sal as member
function"""

class Employee:

    def __init__(self, name, id, designation, salary):
        self.name = name
        self.id = id
        self.designation = designation
        self.salary = salary

    def __str__(self):
        return f'{self.name} is {self.designation}'

    def inc_sal(self):

        print("Salary Increment")

        if(self.designation == "Manager"):
            self.salary*=1.5

        elif(self.designation == "Senor Manager"):
            self.salary*=2

        else:
            self.salary*=1.1    

    
    def get_salary(self):
        print(self.name,"has",self.salary)


e = Employee("Ravi", 1, "Manager", 110000)

print(e)

e.get_salary()

e.inc_sal()

e.get_salary()


