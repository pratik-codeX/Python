######################################3
#importing required libraries
########################################
import sys
import os
import time
import schedule

###########################################################
##   
##  Function Name : DirectoryScanner
##  Input         : Name of Directory
##  Description   : Deletes all empty files periodically
##  Data          : 19/7/2026
##  Author        : Pratik Nanaso Raut
##
############################################################

def DirectoryScanner(DirectoryPath = "Marvellous"):

    Boarder = "-"*60
    timestamp = time.ctime()
    LogFileName = "Marvellous%s.log"%(timestamp)

    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    Ret = False
    
    Ret = os.path.exists(DirectoryPath)

    if Ret == False:
        print("Marvellous Automation Error : There is no Such Directory with name ",DirectoryPath)
        return
    
    
    if (Ret == False):
        print("Marvellous Automation Error : It is not a Directory with name ",DirectoryPath)
        return

    print("Log file gets created with name :",LogFileName)

    fobj = open(LogFileName,"w")

    fobj.write(Boarder+"\n")
    fobj.write("Marvellous Automation Script\n")
    fobj.write(Boarder+"\n")

    fobj.write(Boarder+"\n")
    fobj.write("Files from the Directory are : \n\n")
    fobj.write(Boarder+"\n")

    TotalFiles = 0
    EmptyFile = 0

    for FolderName,SubFolder,Filename in os.walk(DirectoryPath):
        for fname in Filename:
            TotalFiles = TotalFiles + 1
           
            fname = os.path.join(FolderName,fname)
            fobj.write(f"{fname}: {os.path.getsize(fname)} bytes\n")

            if((os.path.getsize(fname)) == 0):
                EmptyFile = EmptyFile + 1
                os.remove(fname)

    fobj.write(Boarder+"\n")

    fobj.write(f"Total Files Scanned :{TotalFiles} \n")
    fobj.write(f"Empty Files Scanned :{EmptyFile} \n")

    fobj.write("Log File gets created at :"+timestamp)
    fobj.write("\n"+Boarder+"\n")

    fobj.close()
###########################################################
##   
##  Function Name : Main
##  Input         : Name of Directory
##  Description   : Deletes all empty files periodically
##  Data          : 19/7/2026
##  Author        : Pratik Nanaso Raut
##
############################################################

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

            schedule.every(20).seconds.do(DirectoryScanner,sys.argv[1])
            DirectoryScanner(sys.argv[1])

            while(True):
                schedule.run_pending()
                time.sleep(1)

    else:
        print("Invalid Number of Arguments!!!")
        print("Please use --h or --u for more information")
        
    print(Border)
    print("Thank you for using Automation Script")
    print(Border)

###################################################################3
##
##  Starter of automation Script
##
######################################################################

if __name__ == "__main__":
    main()