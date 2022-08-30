#import matplotlib.pyplot as plt
import Employee as emp

menu_options = {
    1:'Load data from file',
    2:'Add new employee',
    3:'Display list of employee',
    4:'Show employee details',
    5:'Update employee information',
    6:'Delete employee',
    7:'Increase salary of employee',
    8:'Decrease salary of employee',
    9:'Show total employee a month',
    10:'Show total salary a month',
    11:'Show average of salary a month',
    12:'Show average of age',
    13:'Show maximum age',
    14:'Sort list of employee according to salary by ascending',
    15: 'Draw salary according to age',
    16:'Draw average of salary chart by age group',
    17:'Draw percentage of salary by age group',
    18:'Draw percentage of total employee by age group',
    19:'Store data to file',
    'Others': 'Exit program'
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key])

# Khai báo biến lưu trữ những nhân viên
dsNhanVien = []

while(True):
        print_menu()
        userChoice = ''
        try:
            userChoice = int(input('Input choice: '))
        except:
            print('Invalid input, try again')
            continue
        #Check what choice was entered and act accordingly
        if userChoice == 1:
            fr = open('dbemp_input.db',mode='r',encoding='utf-8')
            for line in fr:
                stripLine = line.strip('\n')
                ds = stripLine.split(',')
                maso = ds[0]
                ten = ds[1]
                tuoi = int(ds[2])
                luong = float(ds[3])
                nv = emp.Employee(maso,ten,tuoi,luong)
                dsNhanVien.append(nv)
            fr.close()
        elif userChoice == 2:
           maso = input("Input code: ")
           ten = input("Input name: ")
           tuoi = int(input("Input age: "))
           luong = float(input("Input salary: "))
           nv = emp.Employee(maso,ten,tuoi,luong)
           dsNhanVien.append(nv)
        elif userChoice == 3:
            for item in dsNhanVien:
                item.display()
        
        elif userChoice == 4:
            id = str(input("Input code: "))
            #print (id)
            for item in dsNhanVien:
                if item == id:
                    print (id)
                else: 
                    print ("Không")
            '''
            for item in dsNhanVien:
                if item == id:
                    item.display()
                else:
                    print ("Không có nhân viên mã này")
            '''