class Student:
    def __init__(self, name, current_class, id):
        self.name= name
        self.id=id
        self.current_class=current_class
    def __repr__(self): #__repr__ this function define to representing the value of class which are directly sent from object. If we want to show some information which are send from object and directly print that than we have to use __repr__()
        return f'Student with name {self.name}, class: {self.current_class}, id: {self.id}'

class Teacher:
    def __init__(self, name, id, subject):
        self.name=name
        self.id=id
        self.subject=subject
    
    def __repr__(self) -> str:
        return f'Teacher\'s name: {self.name}, Subject\'s name:{self.subject}, id: {self.id}'
        
class School:
    def __init__(self, name) -> None:
        self.name=name
        self.teachers=[]
        self.students=[]
        
    def add_teacher(self,name, subject):
        id = len(self.teachers) + 101
        teacher=Teacher(name, subject, id)
        self.teachers.append(teacher)
    
    def enroll(self, name, fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id = len(self.students)+1
            student=Student(name,'c',id)
            self.students.append(student)
            return f'{name} is enroll with id: {id}, extra money{fee-6500}'

    def __repr__(self) -> str:
        print('welcome to', self.name)
        for teacher in self. teachers:
            print(teacher)
        
        for student in self.students:
            print(student)
            
        
# alia=Student('Alia', 6, 220)
# print(alia)
# anis=Teacher('Anis', 'C++', 220238063)
# print(anis)
phitron = School('Phirton')
phitron.enroll('Anis', 9000)
phitron.enroll('kaliya', 7000)
phitron.enroll('Baliya', 8000)
phitron.add_teacher('D.das', 'DS')
phitron.add_teacher('SK.das', 'java')
print(phitron)