def Factorial(No):
    Fact = 1

    for no in range(1,No+1):
        Fact = Fact * no

    return Fact

def main():
    Value = 0
    Ret = 0
    Value = int(input("Enter Number : "))

    Ret = Factorial(Value)

    print("Factorial is : ",Ret)

if __name__ == "__main__":
    main()