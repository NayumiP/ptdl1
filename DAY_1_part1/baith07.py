# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:44:48 2020

@author: Administrator
"""

# Dạng: Dữ liệu trên chương trình 
#--> ghi xuống file

'''
Hãy viết chương trình xuất ra file out.txt
các số chẵn nhỏ số n được nhập từ bàn phím.
Biết rằng mỗi dòng thì lưu 1 số
'''
n = int(input('Nhập số n: '))

fw = open('out.txt','w')

for i in range(n):
    if(i%2 == 0):
        fw.write(str(i)+'\r\n')
        
fw.close()
