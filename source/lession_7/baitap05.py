'''
Bài 05: Viết hàm
        def count_upper_lower(str)
    trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str
'''

#ex1
my_string = 'Hello my name\'s minh tan'
lower_count = sum(map(str.islower, my_string))
print(lower_count)

upper_count = sum(map(str.isupper, my_string))
print(upper_count)


#ex2
def count_upper_lower(str):
    upper_count=0
    lower_count=0
    for x in str:
        if x.isupper():
            upper_count+=1
        else:
            lower_count+=1
    print(f'number of upper case letter {upper_count}')
    print(f'number of lower case letter {lower_count}')

result_2 = count_upper_lower(my_string)
print(result_2)