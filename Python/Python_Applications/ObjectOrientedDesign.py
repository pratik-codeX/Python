class Arithematic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Addition(self):
        Ans = self.No1 + self.No2

        return Ans

    def Substraction(self):
        Ans = self.No1 - self.No2

        return Ans

print("Enter First Number :")
Value1 = int(input())

print("Enter Second Number :")
Value2 = int(input())

aobj = Arithematic(Value1,Value2)

Ret = aobj.Addition()
print("Addition is :",Ret)

Ret = aobj.Substraction()
print("Substraction is :",Ret)