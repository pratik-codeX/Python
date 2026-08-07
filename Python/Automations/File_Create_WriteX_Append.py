def main():
    try:
        fobj = open("Demo.txt","a")
        
        print("File gets Opened")

        fobj.write(" Pune Maharashtra")
        
        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in Current Dirctory")
   
if __name__ == "__main__":
    main()