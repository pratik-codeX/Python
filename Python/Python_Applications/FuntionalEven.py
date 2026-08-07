#This is hybrid approach contains funtional and procedural both

CheckEven = lambda No : (No % 2 == 0)
  
def main():
    Value = int(input("Enter Number :"))

    Ret = CheckEven(Value)

    if(Ret == True):
        print("Its Even Number")
    else:
        print("Its Odd Number")

if __name__ == "__main__":
    main()