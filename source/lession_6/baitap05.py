'''
Bài 05: Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử.
        Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict
'''
my_dict = {
    'c1': [10,20,30,40,50,99,43],
    'c2': [54,23,57,3,5,89,2,66],
    'c3': [6,8,9,0,5,3,2,655],
    'c4': [4,34,2,1,1,1,1,843]
}
for i in my_dict:
    print(my_dict[i][4])
