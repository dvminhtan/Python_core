'''
Bài 04: Viết chương trình tìm ra 3 phần tử có key lớn nhất trong dict
'''
import collections
my_dict = {
    1: "Hello", 
    8: "Tan", 
    19:"Van",
    100: "Hung",
    43: "Viet",
    222: "Truc"
}
x = sorted(my_dict)
#new_dict = collections.OrderedDict(sorted(my_dict.items()))

print(x[-3:])