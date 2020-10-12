'''
Bài 11: Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím.
'''
my_list = ['hello','hello, im Tan','hi,you']
# longest_string = max(my_list, key=len)
# print(longest_string)

#EX2:
# Longest String in list
# using loop
max_len = -1
for ele in my_list:
    if len(ele) > max_len:
        max_len = len(ele)
        res = ele
print(f'Maximum length string is : {res}')