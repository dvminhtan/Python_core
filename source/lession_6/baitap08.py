'''
Bài 08: Viết chương trình lấy ra top 3 phần tử có giá trị lớn nhất từ dict
'''
my_dict = {
    1: 3,
    4: 5,
    6: 9,
    2: 7,
    3: 10,
    0: 13
}
my_list = []
new_list = []
count = 0
for key in my_dict:
    my_list.append(my_dict.get(key))
for i in my_list:
    if i == max(my_list) and count <=3:
        count += 1
    new_list.append(i)
    my_list.remove(i)

print(my_list)
print(new_list)