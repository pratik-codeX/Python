def main():
    try:
        fobj = open("Demo.txt","r")
        
        print("File gets Opened")

        print("File offset is :",fobj.tell())


        Data = fobj.read(10)  #array

        print(Data)

        print("File offset is :",fobj.tell())
        
        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in Current Dirctory")
   
if __name__ == "__main__":
    main()