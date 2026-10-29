import os

def main():
    try:
        #fobj.remove() -> Not Applicable
        os.remove("Demo.txt")

    except FileNotFoundError as fobj:
        print("File is not present in Current Dirctory")
   
if __name__ == "__main__":
    main()