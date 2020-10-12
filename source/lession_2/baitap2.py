# Bài 2. Lập chương trình tính các tổng sau:
#     S_1 = 1 + x + x^2 + x^3 + ... + x^n
#     S_2 = 1 - x + x^2 - x^3 + ... + (-1)^n.x^n
#     S_3 = 1 + \dfrac{x}{1!} + \dfrac{x}{2!} + ... + \dfrac{x^n}{n!}
#     Trong đó, n là số nguyên dương và x là một số thực bất kì. Cả 2 đều được nhập từ bàn phímn
#S_1 = 1 + x + x^2 + x^3 + ... + x^n
n = int(input("Nhap vao n: "))
x = float(input("Nhap vao x: "))
total1 = 1.0
multi1 = x
for i in range(1, n):
    total1 += multi1 # 1 + 3 + 9 + 27
    print(multi1, end=" ")
    multi1 = multi1 * x

print('\nTong s_1: %.2f' % total1)

1 + 3 + 3^2 + 3^3
# #S_2 = 1 - x + x^2 - x^3 + ... + (-1)^n.x^n
# total2 = 1
# for i in range(1, n):
#     total2 += pow(-x, i)
#
# print('\nTong s_2: %.2f' % total2)
#
# #S_3 = 1 + \dfrac{x}{1!} + \dfrac{x}{2!} + ... + \dfrac{x^n}{n!}
# total3 = 1.0
# for i in range(1, n + 1):
#     total3 += ((x**i)/i*i)
#
# print('\nTong s_3: %d' % total3)

