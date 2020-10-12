'''
Bài 06: Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict
'''
my_dict1 = {'a': 1, 'c': 3, 'b': 2}
my_dict2 = {'a': 1, 'b': 2}

for (key, value) in set(my_dict1.items()) & set(my_dict2.items()):
    print('%s: %s ' % (key, value))