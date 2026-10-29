#generic exception handler

def main():
    Ans = 0
    try:
        print("Enter First Number :")
        No1 = int(input())

        print("Enter Second Number :")
        No2 = int(input())
        
        Ans = No1 / No2

        print("Division is Successfull")

    except Exception as eobj:                           #generic Exception block
        print("Exception occured :",eobj)

    print("Result is : ",Ans)

if __name__ == "__main__":
    main()