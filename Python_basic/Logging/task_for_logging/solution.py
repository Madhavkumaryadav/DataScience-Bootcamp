import logging 
import os 

logging.basicConfig(
    filename="task_log.log",
    level=logging.INFO,
    format='%(asctime)s %(message)s'
)


def sum_num(*args):
    
    logging.info("Function is started ....")
    result=sum(args)
    logging.info(f"User input is {args}")
    logging.info(f"Result is {result}")
    return result 

def read_log():
    path='task_log.log'
    f=open(path,'r')
    
    return f.read() 


print(sum_num(3,4,5,6,7,5,4))
print(read_log())
