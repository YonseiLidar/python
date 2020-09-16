variable = 'module_6.py is imported'
print(variable)


class Student():
    
    def __init__(self, name, subject, gender, salary):
        self.name = name
        self.subject = subject
        self.gener = gender
        self.salary = salary  
        
    def raise_salary(self, amount):
        self.salary += amount
        
    def add(self, item):
        if item not in self.subject: 
            self.subject += [item]
            
    def drop(self, item):
        try:
            self.subject.remove(item) 
        except:
            print(f'{self.name}, {item} 수강리스트에 없어요. 정신 차리세요.')
            
def f(a,b):
    return a+b