'''
Cú pháp vòng lặp sẽ giúp cho chúng ta có khả năng truy xuất
đến từng phần tử trong danh sách, tập hợp...nói chung
gọi là collection
Về mặt kỹ thuật chúng ta có 2 cách sử dụng cấu trúc lặp
1. for
2. while
'''
'''
Liệt kê danh sách các kí tự trong một (word)
'''
str = 'Hello'
for c in str:
    print(c)

'''
Hãy in các giá trị trong danh sách
'''
ds = [12, "Hello", 50.5, 0, "today"]
for x in ds:
    print(x)
'''
Có danh các số nguyên
Hãy in ra màn hình các số chẵn
'''
dsSoNguyen = [100, 50, 13, 4, 7]
for x in dsSoNguyen:
    if x%2 == 0:
        print(x)

'''
Hãy in ra tất cả các kí n trong một chuỗi
'''
str = "Today is sunday, my name is Nam"
for c in str:
    if c == 'n':
        print(c)
'''
Hãy đếm xem trong một chuỗi có bao nhiêu kí tự n
'''
str = "Today is sunday, my name is Nam"
dem = 0
for c in str:
    if c == 'n':
        dem = dem+1
print(dem)

