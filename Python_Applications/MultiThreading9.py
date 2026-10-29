#get_ident() is not that reliable to get tid 

import time
import threading

def SumEven(No):
    print("Pid of SumEven Thread is :",threading.get_ident())

def SumOdd(No):
    print("Pid of SumOdd Thread is :",threading.get_ident())
    

def main():
    print("Pid of Main Thread is :",threading.get_ident())

    start_time = time.perf_counter()

    t1 = threading.Thread(target=SumEven,args=(100000000,))
    t2 = threading.Thread(target=SumOdd,args=(100000000,))
 
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    end_time = time.perf_counter()

    print(f"Time required is : {end_time-start_time :.4f}")

if __name__ == "__main__": 
    main()