'''
Bài 08: Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không.
'''
my_tuple_1 = ['tan','tan','tan']
my_tuple_2 = ['tan', 'tan', 'hung']
result_1 = all(x == my_tuple_1[0] for x in my_tuple_1)
result_2 = all(x == my_tuple_2[0] for x in my_tuple_2)
print(result_1)
print(result_2)