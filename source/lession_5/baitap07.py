'''
Bài 07: Viết chương trình kiểm tra 2 tuple có phần tử chung hay không.
'''
my_tuple_1 = (1, 'a', (2, 'b'), 3, 'c', 4)
my_tuple_2 = (1, (2, 'b'), 4, 8)
new_tuple = tuple(set(my_tuple_1) & set(my_tuple_2))
print(new_tuple)