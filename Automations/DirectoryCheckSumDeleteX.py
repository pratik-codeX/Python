import sys
import os
import hashlib

def CalculateChecksum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName):
    Ret = False
    Duplicate = {}

    Ret = os.path.exists(DirectoryName)

    if Ret == False:
        print("Path is Invalid")
        return

    Ret = os.path.isdir(DirectoryName)

    if Ret == False:
        print("It is not a Directory")
        return

    for FolderName,Subfolder,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)

            Cheksum = CalculateChecksum(fname)

            if Cheksum in Duplicate:
                Duplicate[Cheksum].append(fname)
            else:
                Duplicate[Cheksum] = [fname]

    return Duplicate

def DeleteDuplicate(DirectoryName):
    myDict = FindDuplicate(DirectoryName)

    Result = list(filter(lambda x  : len(x) > 1, myDict.values()))

    Count = 0
    Cnt = 0
    TotalDeleted = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if Count > 1:
                print("Duplicate Found",subvalue)
                TotalDeleted = TotalDeleted + 1
        Count = 0

    print("Total Deleted Files : ",TotalDeleted)

    
def main():
    DeleteDuplicate("Test")
    
if __name__ == "__main__":
    main()