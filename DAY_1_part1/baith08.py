# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:53:41 2020

@author: Administrator
"""
# Bài tập tổng hợp
'''
Đọc file dữ liệu num_input.csv
Hãy lưu trữ các số trong file 
vào chương trình. 
Sau đó, xuất ra màn hình
tổng của các số trong file
'''
ds_num = [] # ds_num là một list- danh sách

fr = open('num_input.csv')

flines = fr.readlines()

for line in flines:
    ds_num = ds_num + line.strip().split(',')
    
print(ds_num)

ds_num = [int(i) for i in ds_num]

print(ds_num)

s = 0

for val in ds_num:
    s = s + val

print('Tổng s là: ',s)

