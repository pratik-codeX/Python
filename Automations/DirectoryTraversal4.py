import os

def main():
    for FolderName,SubFolder, FileName in os.walk("/"):
        for FName in FileName:
            print("File name :",FName)

if __name__ == "__main__":
    main()