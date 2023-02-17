# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:17:44 2022

@author: Vaibhav Tiwari
"""

class Fibonaccie():
    def __init__(self,n):
        self.n=n

    def fib(self,n):
        assert n==int(n),"Enter an integer value"
        if(n<1):
            return 1
        return(f.fib(n-1)+f.fib(n-2))                
n=8
f=Fibonaccie(n)
for i in range(n):
    print(f.fib(i))