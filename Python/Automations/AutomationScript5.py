import sys

def main():
    print("------------------------------------------------------")
    print("Marvellous Automation Script")
    print("------------------------------------------------------")

    if (len(sys.argv) == 2):
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation Script is used to Travel the Directory")
            print("For Better usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("*"*15,"Please Execute the Script as :","*"*15)
            print("*"*15,"Python FileName.py DirectoryName","*"*15)
            print("*"*15,"Directory Name should be Absolute path","*"*15)
        else:
            DirectoryName = sys.argv[1]
            print("Directory Name is :",DirectoryName)
    else:
        print("Invalid Number of Arguments!!!")
        print("Please use --h or --u for more information")
        
    print("------------------------------------------------------")
    print("Thank you for using Automation Script")
    print("------------------------------------------------------")

if __name__ == "__main__":
    main()