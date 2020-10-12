#cach 1
n = int(input("Nhập số có không quá 3 chữ số: "))
đơn_vị, chục, ngàn = n % 10, (n % 100) // 10, n // 100
tổng = đơn_vị + chục + ngàn
print("Tổng các chữ số là:", tổng)

#cach 2
n = int(input("Nhập số có không quá 3 chữ số: "))
tổng = 0

tổng += n % 10; n //= 10
tổng += n % 10; n //= 10
tổng += n % 10; n //= 10

print("Tổng các chữ số là:", tổng)

#Cach 3
n = int(input("Nhập số có không quá 3 chữ số: "))
tổng = 0

for _ in range(3):
    tổng += n % 10
    n //= 10

print("Tổng các chữ số là:", tổng)

#cach 4
n = int(input("Nhập số nguyên không âm: "))
tổng = 0

while n > 0:
    tổng += n % 10
    n //= 10

print("Tổng các chữ số là:", tổng)
