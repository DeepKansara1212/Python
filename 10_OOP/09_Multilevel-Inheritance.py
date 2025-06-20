class Employee: 
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

class Job:
    def __init__(self, salary):
        self.salary = salary

class EmployeePersonJob(Employee, Job):  
    def __init__(self, name, emp_id, salary):
        Employee.__init__(self, name, emp_id)  
        Job.__init__(self, salary)       

class Manager(EmployeePersonJob):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department 