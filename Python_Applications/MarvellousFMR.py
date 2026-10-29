CheckEven = lambda No:(No % 2 == 0)
Increment = lambda No: No + 1
Addition = lambda No1,No2 : No1 + No2

def filterX(Task,Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)  #CheckEven(no)

        if Ret == True:
            Result.append(no)

    return Result

def mapX(Task,Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)      #increment(no)
        Result.append(Ret)

    return Result

def reduceX(Task,Elements):
    Sum = 0

    for no in range(Elements):  
        Sum = Task(Sum,no)      #Increment(Sum,no)

    return Sum

def main():
    Data = [13,12,8,10,11,20]

    print("Input Data is : ",Data)

    FData = list(filterX(CheckEven,Data))    #typecast kely list madhe

    print("Data After Filter :",FData)

    MData = list(mapX(Increment,FData))

    print("Data After Map",MData)

    RData = reduceX(Addition,MData)

    print("Data After Reduce :",RData)


if __name__ == "__main__":
    main()