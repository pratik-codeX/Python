import pandas as pd
from pandas import array

def main():

   sobj = pd.Series([27000,32000,35000],index = ["Sagar","Sagar","Pooja"])

   print(sobj)

   print("Salary  : ",sobj["Sagar"])

if __name__ == "__main__":
    main()