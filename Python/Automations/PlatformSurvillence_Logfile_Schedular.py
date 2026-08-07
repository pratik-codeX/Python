import psutil
import sys
import os
import time
import schedule

def PlatformSurvillence(FolderName):
    Boarder = "-"*50
    Ret = False

    Ret = os.path.exists(FolderName)

    if (Ret == True):
        Ret = os.path.isdir(FolderName)
        if Ret == False:
            print("Unable to proceed as directory name is existing but its not a Directory")
            return
    else:
        os.mkdir(FolderName)
        print("Directory For the Log file gets created succesfully")

    ###############

    timestamp = time.strftime("%Y-%m-%d_%H:%M:%S")

    filename = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)

    fobj = open(filename,"w")

    print(f"Log file gets Succesfully created with name {filename}")

def main():
    Boarder = "-"*50

    print(Boarder)
    print("--------Marvellous Platform Survillence System--------")
    print(Boarder)

    #--h and --u handling
    if(len(sys.argv) == 2):
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This Automation Script is used to perform")
            print("1 : It Fetch the Information of Running Processes")
            print("2 : It Fetch the information about Primary Storage as RAM")
            print("3 : It Fetch the information about Secondary Storage as HDD")
            print("4 : It fetch the information about microprocessor")
            print("5 : It gets auto schedule automatically")
            print("6 : It maintains all records into log file")
            print("7 : It send log files through mail periodically")

        elif(sys.argv[1] == "--u"or sys.argv[1] == "--U"):
            print("Use the Automation Script as :")
            print(f" python {sys.argv[0]} time_interval folder_name ")
            print(" time_interval : Time in minutes for periodic execution ")
            print(" folder_name : Name of folder for log file creation ")
        else:
            print("Unable to Proceed as there is no Matching Argument")
            print("Please use --h or --u flag for getting more details")
    #Actual Project Code
    elif(len(sys.argv) == 3):

        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillence,sys.argv[2])

        while(True):

            schedule.run_pending()

            time.sleep(1)

        #PlatformSurvillence(sys.argv[2])
    else:
        print("Invalid Number of Arguments!!!")
        print("Unable to Proceed as Arguments are not matching")
        print("Please use --h or --u flag for getting more details")


    print(Boarder)
    print("------Thank You For Using our Automation System------")
    print(Boarder)

if __name__ == "__main__":
    main()