def CheckEven(No):
    if(No % 2 == 0):
        print("Its Even Number")
    else:
        print("Its Odd Number")

def main():
    Value = int(input("Enter Number :"))

    CheckEven(Value)

if __name__ == "__main__":
    main()