def CheckEven(No):
    return (No % 2 == 0)

def Increment(No):
    return No + 1

def main():
    Data = [13,12,8,10,11,20]

    print("Input Data is : ",Data)

    FData = list(filter(CheckEven,Data))    #typecast kely list madhe

    print("Data After Filter :",FData)

    MData = list(map(Increment,FData))

    print("Data After Map",MData)


if __name__ == "__main__":
    main()