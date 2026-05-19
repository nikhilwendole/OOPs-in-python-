
class person:
    def __init__(self,name,rollno,div):
        self.name=name
        self.rollno=rollno
        self.div=div

class student(person):
    def __init__(self,name,rollno,div,marks,grade):
        super().__init__(name,rollno,div)
        self.marks=marks
        self.grade=grade
    
    def show(self):
        print("Name of the student=",self.name)
        print("Name of the rollno=",self.rollno)
        print("Name of the div=",self.div)
        print("Name of the marks=",self.marks)
        print("Name of the grade=",self.grade)

stud1=student("asdf",1234,2,89,"A")
stud1.show()


