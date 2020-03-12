class Student:
    def __init__(self,a,b):
        self.rollno=a
        self.name=b
    def printvalues(self):
        print("rollno=",self.rollno)
        print("name=",self.name)
s1=Student(24,'Anii')
s1.printvalues()
