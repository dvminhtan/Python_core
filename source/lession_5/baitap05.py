'''
Bài 05: Viết chương trình tìm ra tuple có phần tử thứ 2 là nhỏ nhất từ một list chứa các tuple.
'''

# min and max in list of tuples
# using min() and max()

# initializing list
my_list = [(2, 3), (4, 7), (8, 11), (3, 6)]
# printing original list
print ("The original list is : " + str(my_list))

result = min(my_list[1])
print(f"The min of index 2: {result}")