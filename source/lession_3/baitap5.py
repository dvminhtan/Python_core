#Bài 05: Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bán phím.
#Python3 program to find largest and smallest characters in a string
"""
Input : minh tan
Output : Largest = t, Smallest = a
"""

#cach 1:
s_05 = input("Nhập vào một chuỗi: ")
# if s_05:
#     c_max, c_min = s_05[0], s_05[0]
#     for c in s_05:
#         if c > c_max:
#             c_max = c
#         elif c < c_min:
#             c_min = c
#     print(f"Ký tự lớn nhất {c_max} và nhỏ nhất {c_min}")
# print('Bài 05 - DONE!')  # Bài này có thể dùng hàm max()/min()

#cach 2
# print(f'ky tu lon nhat {max(s_05)}')
# print(f'ky tu nho nhat {min(s_05)}')

#cach 3
def max_alphabet(a, n):
    max = 'A'
    for i in range(n):
        if a[i] > max:
            max = a[i]
    return max

def min_alphabet(a, n):
    min = 'z'
    for i in range(n - 1):
        if a[i] < min:
            min = a[i]
    return min
size = len(s_05)
print(f'Largest alphabet is: {max_alphabet(s_05,size)}')
print(f'smalles alphabet is: {min_alphabet(s_05,size)}')