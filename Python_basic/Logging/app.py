import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
    
)

logger=logging.getLogger('ArithmethicApp')


def add(a,b):
    result=a+b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result
def sub(a,b):
    result=a-b
    logger.debug(f"Adding {a} - {b} ={result}")
    return result

def mul(a,b):
    result=a*b
    logger.debug(f"Adding {a} x {b} = {result} ")
    return result

def div(a,b):
    result=a/b
    logger.debug(f"Adding {a} / {b}  = {result}")
    return result

def view():
    print("1. Adding ")
    print("2. subtrating ")
    print("3. Multiplying ")
    print("4. Dividing")
    
while True:
    view()
    option=int(input("Enter the option : "))
    if option==1:
        a=int(input("Enter first number : "))
        b=int(input("Enter Second number : "))
        res=add(a,b)
        print(res)
    elif option==2:
        a=int(input("Enter first number : "))
        b=int(input("Enter Second number : "))
        res=sub(a,b)
        print(res)
    elif option==3:
        a=int(input("Enter first number : "))
        b=int(input("Enter Second number : "))
        res=mul(a,b)
        print(res)
    elif option==4:
        a=int(input("Enter first number : "))
        b=int(input("Enter Second number : "))
        res=div(a,b)
        print(res)
    elif option==5:
        break
    else:
        print("Invalid Input ")
    
        
        