def main():
    Marks = [78,90,56,98,77]

    for no in Marks:
        print(no)

    Marks[2] = 59
    print("-"*50)       #its not multiplication but tell print * 15 times

    for no in Marks:
        print(no)

if __name__ == "__main__":
    main()