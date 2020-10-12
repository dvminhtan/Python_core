# Bài 06: Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong một chuỗi.
#Python Program to Convert Uppercase using ASCII Values
#Python Program to Convert Lowercase String to Uppercase
"""
input: MINH TAN
output: minh tan
or
input minh tan
output MINH TAN
"""
#Cach 1
s_06 = input("Nhập vào một chuỗi: ")
# s_new = ""
# for c in s_06:
#     if 'a' <= c <= 'z':
#         s_new = s_new + chr(ord(c) - 32)
#     elif 'A' <= c <= 'Z':
#         s_new = s_new + chr(ord(c) + 32)
#     else:
#         s_new = s_new + c
# print("Chuỗi mới: " + s_new)
# print('Bài 06 - DONE!')

#Cach 2
# string1 = s_06.upper()
# string2 = s_06.lower()
# print("\nOriginal String in Lowercase  =  ", string1)
# print("The Given String in Uppercase =  ", string2)

#Cach 3
if s_06.isupper() == False:
	result = s_06.upper()
	print(result)
elif s_06.islower() == False:
    result = s_06.lower()
    print(result)

