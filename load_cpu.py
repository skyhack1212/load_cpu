#coding:utf-8
import time
import os
import math
import multiprocessing
import random



def worker():
    while True:
        math.sin(math.radians(random.randint(30,180)))
        
def run():
    for i in range(1,25):
        multiprocessing.Process(target=worker).start()
    

if __name__== '__main__':
    run()
