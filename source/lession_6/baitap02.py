'''
Bài 02: Viết chương trình sắp xếp các phần tử của dict theo chiều tăng dần của key
'''
#Ex1:
my_dict = {
    'a': 1000,
    'x' : 500,
    'y' : 5001,
    'z' : 250
}
new_dict = {k : v for k, v in sorted(my_dict.items(),key=lambda item: item[1])}
print(new_dict)
#Ex2:
