# seek(kuthe,kuthun)
# Kuthun : 0/1/2


# 0 : Starting
# 1 : Current
# 2 : End

def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets Opened")

        fobj.seek(10,0)

        Data = fobj.read()

        print(Data)

    except FileNotFoundError as fobj:
        print("File is not present in Current Dirctory")
   
if __name__ == "__main__":
    main()