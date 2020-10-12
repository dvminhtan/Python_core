'''
Bài 02: Viết hàm
        def reverse_string(str)
    trả lại chuỗi đảo ngược của chuỗi str
'''
#ex1:
def reverse_string(str):
    return str[::-1]

my_string = ('Hello im Tancool')
result_1 = reverse_string(my_string)
print(f'The reversed string ex1 is: {result_1}')

#ex2:
def reverse(x):
    str = ''
    for i in x:
        str = i + str
    return str
# x = "Hello new day"
result_2 = reverse(my_string)

print(f'The reversed string ex2 is: {result_2}')

#ex3:
def reverse_ex3(x):
    if len(x) == 0:
        return x
    else:
        return reverse_ex3(x[1:]) + x[0]

result_3 = reverse_ex3(my_string)

print(f'The reversed string ex3 is: {result_3}')

#ex4:
def reverse_ex4(x):
    string = "".join((reverse(x)))
    return string

result_4 = reverse_ex4(my_string)
print(f'The reversed string ex3 is: {result_4}')