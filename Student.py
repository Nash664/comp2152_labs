from Person import Person   

class Student(Person):
    def __init__(self, name,age,height,major):
        super().__init__(name,age,height)
        self.major=major
        
        print("This Time its a Student object")



student1 = Student("Maria",22,6,"Computer Science") 
print(student1.name)
print(student1.major)