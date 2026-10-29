class Base1:
    def Fun(self):
        print("Inside Base1 Fun")

class Base2:
    def Gun(self):
        print("Inside Base2 Gun")

class Derived(Base1,Base2):  
    def Sun(self):
        print("Inside Derived Sun")
    
dobj = Derived()

dobj.Fun()
dobj.Sun()
dobj.Gun()