class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role:", self.role)
        print("dept:", self.dept)
        print("Salary:", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", '75000')

# e1 = Employee("Engineer",'IT', '80000')
# e1.showDetails()

eng1 = Engineer("Rohan", '40')
eng1.showDetails()
