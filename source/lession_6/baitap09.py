'''
Bài 09: Viết hàm đếm số lần xuất hiện các ký tự trong một String
Ví dụ:
    Input: ‘Stringings’
    Output: {‘S’: 1, ‘t’: 1, ‘r’: 1, ’i’: 2, ‘n’: 2, ‘g’: 2, ‘s’: 1}
'''
my_string = "Stringings"
new_string = {}
for i in my_string: 
    if i in new_string: 
        new_string[i] += 1
    else: 
        new_string[i] = 1

print(f"Count of all characters {new_string}")