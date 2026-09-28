class Base:
    def Fun(self):
        print("Inside Base Fun")

class Derived(Base):  
    def sun(self):
        print("Inside Derived Sun")
    
dobj = Derived()

dobj.Fun()
dobj.sun()