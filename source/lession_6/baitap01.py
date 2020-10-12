'''
Bài 01: Viết chương trình tìm giá trị lớn nhất và giá trị nhỏ nhất của trường value trong một dict
'''
my_dict = {
    'x' : 500,
    'y' : 5001,
    'z' : 250
}
key_max = max(my_dict.keys(),key=lambda k: my_dict[k])
key_min = min(my_dict.keys(),key=lambda k: my_dict[k])
print(f'Maximun value: {my_dict[key_max]}')
print(f'Minimun value: {my_dict[key_min]}')