# python ProcessSurvillence.py      2           MarvellousLog
# python ProcessSurvillence.py time_interval    Folder_name          
#                   0               1               2
#len(sys.argv) --> 3

# python ProcessSurvillence.py --h
# python ProcessSurvillence.py --u
#                  0             1
#len(sys.argv) --> 2

import psutil
import sys
import os

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
        pass
    else:
        print("Invalid Number of Arguments!!!")
        print("Unable to Proceed as Arguments are not matching")
        print("Please use --h or --u flag for getting more details")


    print(Boarder)
    print("------Thank You For Using our Automation System------")
    print(Boarder)

if __name__ == "__main__":
    main()