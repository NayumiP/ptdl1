# -*- coding: utf-8 -*-
"""
Created on Tue May 17 17:57:10 2022

@author: APTECH
"""

# List comprehension
# Mục đích: Giúp thao tác lấy dữ liệu và trả về kết quả là một danh sách
# một cách nhanh chóng

myCharacter = ['a','b','c','d','e','f','g','h']

'''
Tạo ra một list mới mang tên myUpper chứa 
các chuỗi trong myCharacter
nhưng được viết hoa
'''
myUpper = [x.upper() for x in myCharacter]

print(myCharacter)
print(myUpper)




