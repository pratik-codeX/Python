def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets Opened")

        Data = fobj.read(5)
        print(Data)

        fobj.seek(10,1)

        Data = fobj.read(5)
        print(Data)

    except FileNotFoundError as fobj:
        print("File is not present in Current Dirctory")
   
if __name__ == "__main__":
    main()