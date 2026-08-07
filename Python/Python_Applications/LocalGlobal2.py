no = 11         #Global Variable

def Display():
    a = 21                          #local Variable
    print("From Display : ",no)
    print("From Display Value of a is :",a)

def Demo():
    print("From Demo Value of a is :",a)
    print("From Demo : ",no)

Display()
Demo()