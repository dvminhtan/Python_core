'''
Bài 09: Viết hàm
        def change_upper_lower(str)
    chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str
'''

def swap_case(s):
    swapped = []

    for char in s:
        if char.islower():
            swapped.append(char.upper())
        elif char.isupper():
            swapped.append(char.lower())
        else:
            swapped.append(char)

    return ''.join(swapped)

my_string = "hello im minh tan"
my_string_1 = "HELLO IM MINH TAN"
print(swap_case(my_string_1))