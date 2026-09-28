#5 = 1*3+2*3+3*3+4*3+5*3

import time

def SumCube(No):
    Sum = 0
    for i in range(1,No+1):
        Sum = Sum + (i**3)

    return Sum
        

def main():
    Data = [10000000,20000000,30000000,40000000,50000000]
    Result = list()

    Start_Time = time.perf_counter()


    for Value in Data:
        Ret = SumCube(Value)

        Ret = Result.append(Ret)

    End_Time = time.perf_counter()

    print("Result is :")
    print(Result)
    print(f"Time Require :{End_Time-Start_Time:.4f} Seconds")

 

if __name__ == "__main__":
    main()