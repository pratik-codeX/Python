import numpy as np
from sklearn.linear_model import LinearRegression

def main():
    X = np.array([[1],[2],[3],[4],[5]])     # hr of study

    Y = np.array([50,55,60,65,70])          #marks after each hr of study

    model = LinearRegression(X,Y)

    model = model.fit(X,Y)

    print(model.predict([[6]]))

if __name__ == "__main__":
    main()