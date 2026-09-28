from Marvellous import Addition,Substration

def main():
    print("Enter First Number :")       
    Value1 = int(input())
    
    print("Enter Second Number :")
    Value2 = int(input())

    Ret = Addition(Value1,Value2)
    print("Addition is :",Ret)

    Ret = Substration(Value1,Value2)    
    print("Substration is :",Ret)

if __name__ == "__main__":
    main()
