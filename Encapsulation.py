
class employee():
    def __init__(self,name,employeeid,salary):
        self.name =name
        self.employeeid=employeeid
        self.__salary=salary

class login(employee):
        def __init__(self,name,amount):
            self.__salary+=amount
            self.name=name
            print(self.name,"is logg in ")

class salary(employee):
        def salay(self,amount):
            # self.name=name
            # self.employeeid=employeeid
            self.salary+=amount
employ1=employee("rahul",1234,32000)
employ2=login("rahul",2030202)
employ1.login("rahul",20000)