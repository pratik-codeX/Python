import os

def main():
    for FolderName,SubFolder, FileName in os.walk("Marvellous"):
        print("Folder Name : ",FolderName)
        
        for Subf in SubFolder:
            print("SubFolder name : ",Subf)

        for FName in FileName:
            print("File name :",FName)

if __name__ == "__main__":
    main()