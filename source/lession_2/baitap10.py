"""
Nhập n (n >= 1). In n số đầu tiên trong dãy Fibonacy. Biết nguyên tắc của dãy Fibonacy như sau:
a[0] = a[1] = 1
a[n] = a[n – 1] + a[n – 2]
Vd: Dãy Fibonacy bình thường là: 1 1 2 3 5 8 13 21 34 55 89 144 233
Test 1: Nhập n = 3 => in ra là: 1 1 2
Test 2: Nhập n = 7 => in ra là: 1 1 2 3 5 8 13
Test 3: Nhập n = 1 => in ra là 1
"""
n = int(input("Nhap n: "))
while True:
    if n < 1:
        print("Nhap sai nhap lai!")
        n = int(input("Nhap lai n >= 1: "))
        continue
    break

a1, a2 = 1, 1
if n == 1:
    print(f'a1 = {a1}')
elif n == 2:
    print(f'a1 = {a1} a2 = {a2}')
else:
    print(f'a1 = {a1} a2 = {a2}')
    #n = 3 => lap 1 lan de tim ra a3
    #n = 4 => lap 2 lan de tim ra a4
    #n = 5 => lap 3 lan de tim ra a5
    for i in range(1, n - 1):
        an = a1 + a2
        a1 = a2
        a2 = an
        print(f'an= {an}')
