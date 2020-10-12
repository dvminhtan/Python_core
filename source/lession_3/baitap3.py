#Bài 03: Viết chương trình để xóa bỏ các ký tự có chỉ số là số lẻ trong một chuỗi.
#Write a Python program to remove the characters which hava odd index values of a given string

"""
input:
a b c d e f
0 1 2 3 4 5
output:
ace
"""
#Cach 1
s_03 = input("Nhập vào một chuỗi: ")
# s_new = s_03[0::2]
# print("Chuỗi mới: " + s_new)
# print('Bài 03 - DONE!')

#Cach 2
def odd_values_string(string):
    result = ""
    for i in range(len(string)):
        if i % 2 == 0:
            result += string[i]
    return result

print(odd_values_string(s_03))
