import sys 

if(len(sys.argv) == 3):

    No1 = int(sys.argv[1])
    No2 = int(sys.argv[2])

    Ans = No1 + No2

    print(type(No1))
    print("Addition is ",Ans)
else:
    print("Invalid Number of Arguments...")