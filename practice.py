class restaurant:
    def __init__(self):
        self.name=input("Enter your good name")
        self.menu()
        
    def menu(self):
        self.name=input("Enter your name")
        user_input=input("""
             `f hello, what you would like to eat ,{self.name}
                   1.break fast
                   2.lunch 
                   3.dinner
                   4.tea or coffee
                   
""")
        if user_input=="1":
            self.breakfast()
        elif user_input=="2":
            self.lunch()
        elif user_input=="3":
            self.dinner()
        else:
            print("please input valid number")

        
        
        
    def lunch(self):
        print("""
            1.panner 
              2.tofu
              3.rajma chawal 
           """)
        
    def breakfast(self):
        print("""  
              1.poha
              2.upma 
              3.idli
              4.dosa
               """)
    def dinner(self):
        print("""
              1.panner 
              2.shev bhaji
              3.panner angara
              4.veg thali
              5.non veg thali""")

    
user1=restaurant()
