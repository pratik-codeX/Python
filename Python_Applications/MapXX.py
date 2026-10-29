CheckEven = lambda No : (No % 2 == 0)

Increment = lambda No: No+1

def main():
    Data = [13,12,8,10,11,20]

    print("Input Data is : ",Data)

    FData = list(filter(CheckEven,Data))

    print("Data After Filter :",FData)

    MData = list(map(Increment,FData))

    print("Data After Map",MData)

if __name__ == "__main__":
    main()

#funtion is considered as first class object interpreter cant differenciat between functional aprocach and procedural