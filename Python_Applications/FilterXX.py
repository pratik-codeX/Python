CheckEven = lambda No : No % 2 == 0

def main():
    Data = [13,12,8,10,11,20]

    print("Input Data is : ",Data)

    FData = list(filter(CheckEven,Data))

    print("Data After Filter :",FData)

if __name__ == "__main__":
    main()