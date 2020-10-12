'''
Bài 00: Viết chương trình tính tích value của các phần tử trong một dict
'''
prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 2,
}
mul = 1
for key in prices:
    mul = mul * prices[key]
print(mul)