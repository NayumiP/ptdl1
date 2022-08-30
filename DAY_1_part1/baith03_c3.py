'''
Khi cần để phát sinh dữ liệu ta dùng hàm range
'''
# Sinh ra các số từ 0 đến 9
print(range(10))
for x in range(10):
    print(x)
'''
Sinh ra các số từ 5 cho tới 10 --> range(5,10)
'''
for x in range(5,10):
    print(x)
# Sinh ra dữ liệu từ 5 đến 67 , biết rằng mỗi dữ liệu
# cách nhau 10 đơn vị và bắt đầu từ 5
for x in range(5,67,10):
    print(x)