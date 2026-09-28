import os
import time
import multiprocessing

def SumEven(No):
    print(f"Pid of SumEven :{os.getpid()}\n PPID of SumEven : {os.getppid()}")
    Sum = 0
    for i in range(2,No,2):
        Sum = Sum + i
    
    print(f"Summation of Even : {Sum}")

def SumOdd(No):
    print(f"Pid of SumOdd :{os.getpid()}\n PPID of SumOdd :{os.getppid()}")

    Sum = 0
    for i in range(1,No,2):
        Sum = Sum + i
    
    print(f"Summation of Odd : {Sum}")

def main():
    print(f"Pid of Main :{os.getpid()}\n PPID of Main : {os.getppid()}")

    start_time = time.perf_counter()

    t1 = multiprocessing.Process(target=SumEven,args=(100,))
    t2 = multiprocessing.Process(target=SumOdd,args=(100,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()   
        
    end_time = time.perf_counter()

    print(f"Time required is : {end_time-start_time :.4f}")

if __name__ == "__main__": 
    main()