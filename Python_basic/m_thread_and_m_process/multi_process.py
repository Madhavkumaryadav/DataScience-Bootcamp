import multiprocessing
import time 

def square():
    for i in range(5):
        time.sleep(2)
        print(f"square : {i*i}")
        
def cube():
    for i in range(5):
        time.sleep(2)
        print(f"Cube {i * i* i}")
        
if __name__=='__main__':
    ## Create 3 Processes 

    p1=multiprocessing.Process(target=square)
    p2=multiprocessing.Process(target=cube)    


    t=time.time()
    ## Start the process 
    p1.start()
    p2.start()


    p1.join()
    p2.join()   

    f_time=time.time()-t
    print(f_time)