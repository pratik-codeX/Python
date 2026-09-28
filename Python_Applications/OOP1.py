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

        print(self.Value1)
        print(self.Value2)


dobj = Demo()
dobj.Fun()