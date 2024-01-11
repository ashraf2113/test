class women:
    def __init__(self,name,age,sons,salary,degree):
        self.name=name
        self.age=age
        self.sons=sons
        self.salary=salary
        self.degree=degree
        
    def degree(self):
        if self.degree >= 4.5:
            return True
        
        else:
            return False
    def bonus(self):
        if self.age >= 60:
            self.salary += 500
            print("he will get bonus and it is new salary is  "  +  str(self.salary))
        else:
            print("It is no bonus and it is salary still  "+  str(self.salary))    
            
               
        
        

                