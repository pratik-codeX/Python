def Summation(Data):
    Sum = 0

    for no in Data:
        Sum = Sum + no

    '''for i in range(len(Data)):
        Sum = Sum + Data[i]
    '''
    return Sum

def main():
    size = 0
    Arr = list()

    print("Enter the Number of elements :")
    size = int(input())

    print("Enter the Elements :")
    
    for i in range(size):
        no = int(input())
        Arr.append(no)

    Ret = Summation(Arr)
    print("Addition is :",Ret)

if __name__ == "__main__":
    main()