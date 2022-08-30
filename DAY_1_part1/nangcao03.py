# -*- coding: utf-8 -*-
"""
Created on Tue May 17 18:25:24 2022

@author: APTECH
"""
'''
Hãy định nghĩa hàm tính lập phương của một số
'''

def lapphuong(x):
    return x**3

kq = lapphuong(10)
print('Kết quả:',kq)

'''
Khi cần cài đặt nhanh chóng các hàm mà 
không cần tốn thời gian định nghĩa
hàm cụ thể ta có thể sử dụng dạng hàm nặc danh (chỉ dùng thời điểm đó, sau đó bị hủy bỏ)
(không có tên và dùng ngay), 
được gọi là ngôn ngữ lambda
'''

ketqua = lambda x: x**3

print('ketqua= ',ketqua(10))