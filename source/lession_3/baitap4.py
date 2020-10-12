#Bài 04: Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào, nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
"""
input:
minh tan
output:
mian
"""

#Cach 1
s_04 = input("Nhập vào một chuỗi: ")
# s_new = ""
# if len(s_04) >= 2:
#     s_new = s_04[0:2] + s_04[-2:]
# print("Chuỗi mới: " + s_new)
# print('Bài 04 - DONE!')

#Cach 2
def string_both_ends(string):
    if len(string) < 2:
        return ''
    return string[0:2] + string[-2:]
print(string_both_ends(s_04))