# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:44:36 2022

@author: Student
"""

import matplotlib.pyplot as plt

dailys = ['Đại lý A','Đại lý B','Đại lý C','Đại lý D','Đại lý E']

doanhthu = [20,25,15,10,20]

noibat = [0,0.1,0,0,0]

plt.pie(doanhthu, explode=noibat, labels=dailys, shadow=True, startangle=45)

plt.axis("equal")

plt.legend(title='Danh sách đại lý')

plt.show()

# Câu hỏi đặt ra: Muốn làm nổi bật đại lý chiếm phần trăm doanh thu cao nhất thì như thế nào?