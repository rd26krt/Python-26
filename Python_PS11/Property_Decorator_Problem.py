class Employee:
    salary = 2400
    increment = 20

    @property
    def salary_after_increment(self):
        return self.salary + (self.salary * self.increment / 100)
    
    @salary_after_increment.setter
    def salary_after_increment(self, value):
        self.increment = ((value - self.salary) / self.salary) * 100
        

e = Employee()
print(e.salary_after_increment) # 2880.0
e.salary_after_increment = 2520
print(e.increment) # 25.0
