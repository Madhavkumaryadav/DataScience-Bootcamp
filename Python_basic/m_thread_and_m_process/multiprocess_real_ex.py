'''
Real-world Example: Multiprocessing for CPU-bound Tasks
scenario : Factorial Calculation
Factorial Calculation , Especially for large numbers,
involve significant computational work. Multiprocessing 
can be used to distribute the workload across multiple 
CUP cores improving performance.


'''


import multiprocessing

import math
import sys
import time

# Increase the maximum number of digits for integer conversion 

sys.set_int_max_str_digits(1000000000)

## Function compute factorials of a given number

def computer_fact(number):
    print(f"Computing Factorial of {number }")
    result=math.factorial(number)
    print(f'Factorial of {number } is {result}')
    return result


if __name__=="__main__":
    number=[50000]
    
    start_time=time.time()
    
    ## create a pool of workers processes
    with multiprocessing.Pool() as pool:
        result=pool.map(computer_fact,number)
        
    end_time=time.time()
    print(f'Results : {result}')
    print(f'Time taken : {end_time-start_time} seconds ')
        