# Hàm cắt chuỗi
a = "hello,world,aptech,fpt,arena"
# Dấu cách các từ vựng được gọi là delimiter (dấu phân cách)
# Các từ vừng mong muốn được tách ra
# khỏi phân cách được gọi là Token
dsToken = a.split(',')
print(dsToken[1])
print(dsToken[3])
print(dsToken[1:3])


