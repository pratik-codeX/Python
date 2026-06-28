def Display(*Data):     #its looks like pointer but its not pointer
    print(Data)
    print(type(Data))

def main():
    Display(10,20.2,"Python",True,50,60,70)

if __name__ == "__main__":
    main()