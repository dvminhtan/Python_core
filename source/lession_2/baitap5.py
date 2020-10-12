"""
Nhập vào 2 số nguyên dương a & b với điều kiện là b > a. Hãy thực hiện các yêu cầu sau:
a. Đếm xem trong đoạn [a, b] có bao nhiêu số đối xứng, chính phương, nguyên tố
b. Tính tổng các số đối xứng, chính phương, nguyên tố trong đoạn [a, b]
"""
import math
a = int(input("Enter your score a: "))
while True:
    try:
        if a < 0:
            print("Nhap lai")
            a = int(input("Enter your score a: "))
        break
    except ValueError:
        print("Int, please.")
#mỗi lần lặp xét i
count = 0
for i in range(2, a+1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        print(i)

# Cach 2
# i = 2
# while i < 100:
#   j = 2
#   while j <= (i/j):
#     if not (i % j):
#         break
#     j += 1
#   if j > i/j:
#       print(i), " is prime"
#   i += 1