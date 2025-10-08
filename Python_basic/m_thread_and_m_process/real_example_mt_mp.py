'''
Real-WOrld Example: Multithreading for I/O-bound tasks 
scienario: web Scrapting we scraping offten involes making numerous networs requests to 
fetch we pages. These tasks are I/O-bound because they spend a lot of 
timme waiting for responses from servers. Multithreading can singifincantly 
improve the performance by allowing multiple we pages t be featched concurrently .

'''
'''
https://leetcode.com/
https://www.udemy.com/course/complete-machine-learning-nlp-bootcamp-mlops-deployment/learn/lecture/44469902#reviews

'''

import threading
import requests
from bs4 import BeautifulSoup

urls=[
    'https://leetcode.com/',
    'https://www.udemy.com/course/complete-machine-learning-nlp-bootcamp-mlops-deployment/learn/lecture/44469902#reviews',
    'https://www.geeksforgeeks.org/data-science/data-science-for-beginners/'

]

def featch_contents(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'featched {len(soup)} characters form {url}')
    
threads=[]
for url in urls:
    thread=threading.Thread(target=featch_contents,args=(url,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()
    
    
print("All web pages ")
    
    