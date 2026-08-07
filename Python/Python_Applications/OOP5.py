class Demo:
    Value1 = 10     #class variables
    Value2 = 20     #class variables

    def __init__(self):
        self.No1 = 11
        self.No2 = 21

    #Instance Method
    def Fun(self):
        print("Inside Instance Method named as Fun")
        print(self.No1)
        print(self.No2)

        print(Demo.Value1)
        print(Demo.Value2)

    @classmethod
    def Gun(cls):
        print("Inside Class Method named as Gun")
        #print(Demo.No1)    Not Allowed
        #print(Demo.No2)    Not Allowed

        print(cls.Value1)
        print(cls.Value2)

# call with object
dobj = Demo()
dobj.Gun()