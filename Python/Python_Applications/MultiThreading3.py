import threading

def Display(No): #Display(*No)  variable number or argument
    print(f"Inside Display {No}: ",threading.get_ident())

def main():
    print("Inside main: ",threading.get_ident())

    tobj = threading.Thread(target = Display,args=(11,))    #we have to pass iterable as argument

    tobj.start()

if __name__ == "__main__": 
    main()