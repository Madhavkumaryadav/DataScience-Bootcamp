## python advanced multiprocessing 

from concurrent.futures import ThreadPoolExecutor
import time

def print_num(number):
    time.sleep(1)
    return f"Number {number}"

number=[i for i in range(20)]

with ThreadPoolExecutor (max_workers=3) as executor:
    results=executor.map(print_num,number)

for result in results:
    print(result)