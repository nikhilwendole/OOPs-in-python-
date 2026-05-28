class student:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Roll_No:",self.roll_number)
        print("Marks:",self.marks)
        self.result()
        
    def result(self):
        if self.marks>40:
            print("congratulation you are passed")
        else:
            print("Better luck next time")
        
college=[]

n = int(input("How many students: "))

for i in range(n):
    name=input("enter the name")
    roll_number=int(input("enter the roll no"))
    marks=int(input("enter the marks"))

    s=student(name,roll_number,marks)
    college.append(s)
    print()

for student in college:
    student.display()
    print() 

