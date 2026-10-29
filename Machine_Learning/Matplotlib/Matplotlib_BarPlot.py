import matplotlib.pyplot as plt

def main():
    language = ["C","C++","Java","Python"]

    students = [30,40,35,55]

    plt.bar(
        language,
        students,
        width=0.6,          #width of bars
        edgecolor = "black",#boarder color of bars
        linewidth = 1,      #width of bar boarder
        alpha = 0.8,        #transperency   0.0 to 1.0
        label = "students" , # legend text
    )

    plt.title("Marvellous Bar Plot")
    plt.xlabel("Languages ")
    plt.ylabel("Number of Students")

    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    main()