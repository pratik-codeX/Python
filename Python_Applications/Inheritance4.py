class Base:
    def __init__(self):
        print("Inside Base Constructor")

    def Fun(self):
        print("Inside Base Fun")

class Derived(Base):  
    def __init__(self):
        super().__init__()
        print("Inside Derived Constructor")
    
dobj = Derived()

dobj.Fun()