
# class employee():
#     def __init__(self,name,employeeid,salary):
#         self.name =name
#         self.employeeid=employeeid
#         self.__salary=salary

# class login(employee):
#         def __init__(self,name,amount):
#             self.__salary+=amount
#             self.name=name
#             print(self.name,"is logg in ")

# class salary(employee):
#         def salay(self,amount):
#             # self.name=name
#             # self.employeeid=employeeid
#             self.salary+=amount
# employ1=employee("rahul",1234,32000)
# employ2=login("rahul",2030202)
# employ1.login("rahul",20000)



class ATM:
    def __init__(self):
        self.__pin=input("Enter the pin")
        self.__balance=0

    def get_pin(self):
        return self.__pin
    
    def set_pin(self,newpin):
        self.newpin=input("enter the new pin")
        if newpin<3:
            print("allowed ")
        self.__pin=self.newpin
        print("pin changed successfully",self.__pin)

sbi=ATM()
sbi.get_pin()
sbi.set_pin(1233)