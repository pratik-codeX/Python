def main():
    try:
        fobj = open("Demo.txt","r")
        
        print("File gets Opened")

        Data = fobj.read(10)  #array

        print(Data)
        
        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in Current Dirctory")
   
if __name__ == "__main__":
    main()