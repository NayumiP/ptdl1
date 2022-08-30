# -*- coding: utf-8 -*-
"""
Created on Tue May 17 18:33:23 2022

@author: APTECH
"""

'''
(*) Ứng dụng của lambda trong filter (lọc dữ liệu theo điều kiện) 
dữ liệu
'''

myNumber = [10,5,9,2,8,6,10,8,12]

'''
Hãy lấy ra danh sách các số là số chẵn
'''
myEven = list(filter(lambda x: (x%2 == 0), myNumber))
print(myEven)

'''
Hãy lấy ra danh sách myChanChuc các số là số chẵn 
và chia hết cho 5
'''
myChanChuc = list(filter(lambda x: (x%2 == 0 and x%5 == 0), myNumber))
print(myChanChuc)

'''
Chúng ta dùng lambda trong filter khi điều kiện lọc là hàm phức tạp
hoặc trên tập dự liệu có thể lặp (iterator)
còn nếu hàm đơn giản và dùng trên list thì 
chúng ta có thể dùng list comprhension
'''

'''
Tương tự chúng ta có thể sử dụng map như filter
'''

'''
Hãy tạo ra danh sách myLapPhuong lập phương các số trong myNumber
'''
myLapPhuong = list(map(lambda x: x**3, myNumber))
print(myLapPhuong)








