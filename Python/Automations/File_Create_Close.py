def main():
    try:
        fobj = open("Demo.txt","w")
        
        print("File gets Opened")
        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in Current Dirctory")
   
if __name__ == "__main__":
    main()