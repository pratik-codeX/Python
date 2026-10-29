import sys

def main():
    Border = "-"*60
    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    if (len(sys.argv) == 2):
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation Script is used to Travel the Directory")
            print("For Better usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please Execute the Script as :")
            print("Python FileName.py DirectoryName")
            print("Directory Name should be Absolute path")
        else:
            DirectoryName = sys.argv[1]
            print("Directory Name is :",DirectoryName)
    else:
        print("Invalid Number of Arguments!!!")
        print("Please use --h or --u for more information")
        
    print(Border)
    print("Thank you for using Automation Script")
    print(Border)

if __name__ == "__main__":
    main()