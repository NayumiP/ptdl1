'''
Viết hàm tính các phép tính số học (+,-,*,/) của hai số biết trước
Sau đó, gọi hàm
'''
myname = ""
# Khai báo hàm
def calArithmetic(n,m):
    plus = n+m
    subs = n-m
    mult = n*m
    divs = n/m
    myname = "Mr.Nam"
    print(myname)
    return plus, subs, mult, divs
# Gọi hàm
x,y,z,t = calArithmetic(10,5)
print(f'Tổng là: {x}, hiệu là: {y}, tích là: {z}, thương là: {t}')
#print(plus) # Chúng ta không thể sử dụng biến plus bên ngoài của hàm
# lý do: vì biến plus được khai báo trong thân hàm calArithmetic
# cho nên biến đó chỉ được dùng trong phạm vi (scope) của hàm

myname ="Aptech Ltm"
print(myname)
# Biến myname được xem như là biến toàn cục , có nghĩa là ta có thể sử dụng biến này
# trong toàn bộ chương trình được viết trên file này
# trong khi đó, biến plus được xem là biến cục bộ (chỉ sử dụng trong phạm vi của hàm)