"""Create two classes namely
Employee and Qualification. Using
multiple inheritance derive two
classes Scientist and Manager. Take
suitable attributes & operations.
WAP to implement this class
hierarchy.
"""

class Employee:

    def get_data(self, name, designation):
        self.name = name
        self.designation = designation

    def data_info(self):
        return f'{self.name} is {self.designation}'

class Qualification:

        def get_degree(self, degree):
            self.degree = degree

        def degree_info(self):
            return f'Completed {self.degree}'

class Scientist(Employee,Qualification):

    def get_data(self, name):
        self.name = name
        self.designation = "Scientist"
    pass

class Manager(Employee,Qualification):

    def get_data(self, name):
        self.name = name
        self.designation = "Manager"
    pass


s = Scientist()
s.get_data("Ravi")
s.get_degree("PhD")
print(s.data_info(), s.degree_info())

m = Manager()
m.get_data("Rajiv")
m.get_degree("MBA")
print(m.data_info(), m.degree_info())
