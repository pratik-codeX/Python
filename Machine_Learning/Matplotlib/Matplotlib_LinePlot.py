import matplotlib.pyplot as plt

def main():
    X = [1,2,3,4,5]
    Y = [10,25,18,35,30]

    plt.plot(
        X,          #Postion parameter as value of x axis
        Y,          #position parameter as value of y axis
        marker = "o",           #Line of that 
        linestyle = "--",
        linewidth = 2,
        markersize = 7,
        label = "Marks"
    )

    plt.title("Marvellous Line Plot")

    plt.xlabel("Student Number")

    plt.ylabel("Student Marks")

    plt.grid(False)

    plt.legend()

    plt.show()

if __name__ == "__main__":
    main()