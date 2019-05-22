# -*- coding: utf-8 -*-
"""
Created on Fri May 17 09:27:25 2019
@author: asgupta

Simple add function in python
"""
#import libraies
import numpy as np

#define addition function
def add_func(num1,num2):
    result = num1 + num2
    return(result)

#main funciton
if __name__ == '__main__':
    num1 = 10
    num2 = 20
    add_result = add_func(num1,num2)
    print('Addition:', add_result)
    
   
