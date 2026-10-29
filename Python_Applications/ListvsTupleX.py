#                            List        Tuple      
#-----------------------------------------------------------------
# Ordered                   yes         yes             
# Indexed                   yes         yes
# Mutable or changeble      yes         No
# Heterogenous              yes         yes
def main():
    Data1 = [10,3.14,True,"Pune"]   #List
    Data2 = (10,3.14,True,"Pune")   #Tuple

    print(Data1)
    print(Data2)
    print(Data1[0])
    print(Data2[0])

if __name__ == "__main__":
    main()