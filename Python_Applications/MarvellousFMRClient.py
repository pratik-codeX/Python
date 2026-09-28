from MavellousLibrary import filterX, mapX, reduceX

CheckEven = lambda No:(No % 2 == 0)
Increment = lambda No: No + 1
Addition = lambda No1,No2 : No1 + No2

def main():
    Data = list()

    Size = int(input("Enter Size of Data"))

    for i in range(Size):
        i = int(input())
        Data.append(i)

    print("Input Data is : ",Data)

    FData = list(filterX(CheckEven,Data))    #typecast kely list madhe

    print("Data After Filter :",FData)

    MData = list(mapX(Increment,FData))

    print("Data After Map",MData)

    RData = reduceX(Addition,MData)

    print("Data After Reduce :",RData)


if __name__ == "__main__":
    main()