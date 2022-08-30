'''
(*) Sinh viên tự thực hành
Viết chương trình menu
1- Đọc dữ liệu từ file input.db
2- Thêm mới hình chữ nhật
3- Hiển thị danh sách hình chữ nhật
4- Lưu danh sách hình chữ nhật xuống file demo4output.db
Others- Thoát
'''
import Rectangle as rect
import pandas as pd
import sqlite3
menu = {
    1: 'Đọc dữ liệu từ file input.db',
    2: 'Thêm mới hình chữ nhật',
    3: 'Hiển thị danh sách hình chữ nhật',
    4: 'Lưu danh sách hình chữ nhật xuống file demo4output.db',
    'Others': 'Thoát'
}


def print_menu():
    for key in menu.keys():
        print(key, '--', menu[key])

dsHCN = []

while (True):
    print_menu()
    choice = ''
    try:
        choice = int(input('Nhập lựa chọn của bạn: '))
    except:
        print('Không có lựa chọn này, hãy nhập lại...')
        continue

    if choice == 1:
        # print('Lựa chọn 1')
        fhand = open('input.db')
        for line in fhand:
            print(line) 
       # Thêm mới HCN
    elif choice == 2:
        cr = float(input("Nhập chiều rộng cho hcn: "))
        cd = float(input("Nhập chiều dài cho hcn: "))
       
        hcn = rect.Rectangle(cr, cd)
        dsHCN.append(hcn)
        # Hiển thị ds HCN
    elif choice == 3:
        for item in dsHCN:
            item.display()
        # Lưu ds hcn xuống file demo4output.db
    elif choice == 4:
        fw = open('demo4output.db',mode='w',encoding='utf-8')
        for item in dsHCN:
            fw.write(f'{item.width}-{item.length}-{item.perimeter()}-{item.area()}\n')
        fw.close()
    else:
        print('Thoát chương trình')
        break
