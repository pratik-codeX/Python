def CheckEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False

def main():
    Value = int(input("Enter Number :"))

    Ret = CheckEven(Value)

    if(Ret == True):
        print("Its Even Number")
    else:
        print("Its Odd Number")

if __name__ == "__main__":
    main()