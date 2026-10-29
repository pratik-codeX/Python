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
   
    except ZeroDivisionError as zobj:                   #specific Except block
        print("Exception Occured due to second operand is zero :",zobj)
    
    except ValueError as vobj:                          #specific Except block
        print("Exception occured due to invalid Datatype : ",vobj)

    except Exception as eobj:                           #generci Exception block
        print("Exception occured :",eobj)

    finally:
        print("Inside Finally Block")

    print("Result is : ",Ans)

if __name__ == "__main__":
    main()