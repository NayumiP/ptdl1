# -*- coding: utf-8 -*-
"""
Created on Tue May 17 18:08:59 2022

@author: APTECH
"""

myNumer = [0,1,2,3,4,5,6,7,8,9,10]

'''
Hãy tạo danh sách myGreater5 là các số lớn hơn 5 được
lấy từ myNumber
'''
myGreater5 = [x for x in myNumer if x > 5]
print(myGreater5)

'''
Hãy tạo danh sách mySquare là các số bình phương của các
giá trị được lấy từ myNumber
'''
mySquare = [x*x for x in myNumer ]
print(mySquare)

'''
Hãy tạo danh sách myEven là các số chẵn trong myNumber
'''
myEven = [x for x in  myNumer if x%2 == 0]
print(myEven)
'''
Hãy tạo danh sách myEvenSquare là các bình phương các 
số chẵn trong myNumber
'''
myEvenSquare = [x**2 for x in  myNumer if x%2 == 0]
print(myEvenSquare)



