#python Automation.py --h
#python Automation.py --u
#python Automation.py Marvellous


#python Automation.py --d
#python Automation.py Marvellous Demo


import sys

def main():
    
    if (len(sys.argv) == 2):
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("Help")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("usage")
        else:
            DirectoryName = sys.argv[1]
            print("Directory Name is :",DirectoryName)
    else:
        print("Invalid Number of Arguments!!!")
        print("Please use --h or --u for more information")

if __name__ == "__main__":
    main()