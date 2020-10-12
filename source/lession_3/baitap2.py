# Bài 02: Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím.
"""input:
m i n h t a n
0 1 2 3 4 5 6
output: i = 3
m i n t a n
"""

#Cach 1
s_02 = input("Nhập vào một chuỗi: ")
# if s_02:
#     m = int(input("Vị trí muốn xóa: "))
#     if 0 <= m < len(s_02):
#         s_new = s_02[:m] + s_02[m+1:]
#         print("Chuỗi mới: " + s_new)
#     else:
#         print('Không thể tìm được vị trí cần xóa!')
# print('Bài 02 - DONE!')

#Cach 2
"""
def remove_character(string, i):
    #Characters before the i-th indexed, is stored in a variable a
    a = string[:i]
    #Characters after the nth indexed, is stored in a variable b
    b = string[i + 1:]

    #returning string after removing
    return a + b
i = int(input("Vị trí muốn xóa: "))
print(remove_character(s_02,i))
"""
#Cach 3
def remove_character(string,k):
    for j in range(len(string)):
        if j == k:
            string = string.replace(string[i], "", 1)
    return string
i = int(input("Ví trí muốn xóa: "))
print(remove_character(s_02, i))