'''
Hãy cho biết có bao nhiêu từ love trong câu sau
biết rằng mỗi từ vựng trong câu thì
cách nhau bởi 1 dấu khoảng cách
'''
mysen = 'I love so much I love you too love love everytime and love love everywhere'
# Tiến hành cắt từ vựng và lưu vào danh sách các từ
dsVoc = mysen.split(" ")
dem = 0
for s in dsVoc:
    if s == 'love':
        dem = dem+1
print(dem)