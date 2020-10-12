# Bài 01: Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $.
#Cach 1
s_01 = input("Type something: ")

def manual_replace(s, char, index):
    return s[:index] + char + s[index + 1:]

print(manual_replace (s_01,'$', 0))

#Cach 2
if len(s_01) > 0:
    print(s_01.replace(s_01[0], '$'))

#Cach 3
# string = input("Type something ")
position = 0
new_character = '$'

string = s_01[:position] + new_character + s_01[position+1:]
print(string)