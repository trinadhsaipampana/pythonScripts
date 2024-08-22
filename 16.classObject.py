'''
Declare a class to store the data of employes by declaring object for each employ
Declare a function for provision of salary changes and dept changes
'''

class EmployDetails:
    def __init__(self, name, email, dept, salary):
        self.name=name
        self.email=email
        self.dept=dept
        self.salary=salary
        
    def emp_info(self):
        print(f'Employ name is {self.name}')
        print(f'Employ email is {self.email}')
        print(f'Employ department is {self.dept}')
        print(f'Employ salary is {self.salary}')
    
    def changes_salary(self, salary):
        self.salary=salary
        print(f'Changes made to {self.name} in salary is {salary}')
        
    def changes_dept(self, dept):
        self.dept=dept
        print(f'Changes made to {self.name} in department is {dept}')     
        
                
emp1=EmployDetails('Sai', 'sai@email.com', 'DevOps', 75000)
emp2=EmployDetails('Trinadh', 'trinadh@email.com', 'SecOps', 50000) 

print(emp1.name)
print(emp1.email)
print(emp1.dept)
print(emp1.salary)

print()

emp2.emp_info()

print()

emp1.changes_salary(90000)

print()

emp2.changes_dept('SOC')