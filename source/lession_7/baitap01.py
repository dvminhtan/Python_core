'''
Bài 01: Viết hàm
        def max_min(*numbers)
    trả lại cả giá trị max, min của nhiều số được truyền vào
'''

def _min(*numbers):
    return min(numbers)

def max_(*numbers):
    return max(numbers)

print(_min(56,2,4,89,5,3333,6))
print(max_(56,2,4,89,5,3333,6))