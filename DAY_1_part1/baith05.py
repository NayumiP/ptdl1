# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:11:03 2020

@author: Administrator
"""

'''
Hãy nhập từ bàn phím số tự nhiên n 
và xuất ra màn hình:
    
1. Các số nguyên tố nhỏ hơn n
2. Xuất ra tổng các số nguyên tố nhỏ hơn n
'''
import thuvienham as lib
n = int(input('Nhập n= '))
i = 0
for i in range(n):
    if (lib.isPrime(i) == True):
        print (i)



    
