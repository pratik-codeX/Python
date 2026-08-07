def Factorial(No):
    Fact = 1

    for no in range(1,No+1):
        Fact = Fact * no

    return Fact

def main():
    Value = int(input("Enter Number : "))

    Ret = Factorial(Value)
    print(f"Factorial of {Value} is {Ret}")

if __name__ == "__main__":
    main()