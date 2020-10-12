#Tính giai thừa
n = int(input("Nhập số nguyên dương: "))
f = 1
for i in range(1, n + 1):
    f *= i
print(f"{n}! = {f}")

# cach 2
n = int(input("Nhập số nguyên dương: "))
f, i = 1, 1
while i <= n:
    f *= i
    i += 1
print(f"{n}! = {f}")