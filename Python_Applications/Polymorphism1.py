class Base:
    def Fun(self):
        print("Inside Base Fun")

class Derived(Base):
    def Fun(self):
        print("Inside Derived Fun")

dobj = Derived()
dobj.Fun()