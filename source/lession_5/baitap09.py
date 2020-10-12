'''
Bài 09: Viết chương trình tính tổng và tìm giá trị lớn nhất trong tuple chứa các số thực.
'''
my_tuple = (6.0,9.0,6.9,69.69)
sum = 0
max = my_tuple[0]
for i in my_tuple:
    if max < i:
        max = i
    sum += i

print(sum)
print(max)