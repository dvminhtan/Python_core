'''
Bài 03: Viết chương trình lấy các các giá trị không trùng lặp từ dict
'''
my_dict = {
    'a': 2,
    'b': 5,
    'c': 9,
    'd': 5
}

new_dict = {}
for key, value in my_dict.items():
    if value not in new_dict:
        new_dict[value] = [key]
    else:
        new_dict[value].append(key)
print(new_dict)