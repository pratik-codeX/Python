import os

def main():

    if (os.path.exists("Demo.txt")):
        print("File is Present in Current Directory")
    else:
        print("There is no Such file")
   
if __name__ == "__main__":
    main()