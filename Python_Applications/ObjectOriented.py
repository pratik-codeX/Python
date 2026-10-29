class Arithematic:
    
    def Addition(No1,No2):
        Ans = No1 + No2

        return Ans

    def Substraction(No1,No2):
        Ans = No1 - No2

        return Ans
    
aobj = Arithematic()

print("Enter First Number :")
Value1 = int(input())

print("Enter Second Number :")
Value2 = int(input())

#Ret = Addition(aobj,Value1,Value2) he internally ass janar tyamul aapn self as positional argument jato

Ret = aobj.Addition(Value1,Value2)  #Error
print("Addition is :",Ret)

Ret = aobj.Substraction(Value1,Value2)  #Error
print("Substraction is :",Ret)