
class payment:
    def payment(self,name,modeofcash):
        self.name=name
        self.modeofcash=modeofcash
        print("pay money through online")
    
class upi(payment):
    def payment(self,name,modeofcash):
        self.name=name
        self.modeofcash=modeofcash
        print(self.modeofcash,"payment through that type",self.name)

class onlineCard(payment):
    def payment(self, name, modeofcash):
        self.name=name
        self.modeofcash=modeofcash
        print(self.modeofcash,"payment through that type",self.name)

class cash(payment):
    def payment(self,name,modeofcash):
        self.name=name
        self.modeofcash=modeofcash
        print(self.modeofcash,"payment through that type",self.name)


customer1=onlineCard()
customer1.payment("assf","onlinecard")
customer2=cash()
customer2.payment("qwert","cash")


