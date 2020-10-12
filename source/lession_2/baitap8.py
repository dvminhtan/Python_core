#4. Tìm ước số chung lớn nhất của 2 số nguyên dương a và b nhập từ bàn phím.
"""
The Highest Common Factor (HCF) , also called gcd, can be computed in python using a single function offered by math module and hence can make tasks easier in many situations.
"""

a = int(input("Nhap a: "))
while True:
    if a < 0:
        print("Gia tri a không hợp lệ")
        a = int(input("Nhap lai a: "))
    break

b = int(input("Nhap b: "))
while True:
    if b < 0:
        print("Gia tri b không hợp lệ")
        b = int(input("Nhap lai b: "))
    break

"""
Giả sử ta nói 
Số 4 chia hết cho 1 , 2 , 4
Số 6: chia hết cho các số 1, 2, 3 ,6
ý tưởng ta xét từ số bé nhất và xét các số mà nó chia hết lần lượt
lấy từng số đó so sánh với thằng lớn hơn, nếu thằng lớn hơn cũng chia hết thì thõa
lưu ý: xét từ số lớn về 1. ngay chỏ nào mà thõa thì lập tức dừng lại vi đảm bảo nó  là lớn nhất
"""
#dùng toán tử 3 ngôi trong python như sau
min = a if a < b else b
max = a if a > b else b
cach_1 = 0
ucln = 0
if max % min == 0:
    ucln = min
else:
    for i in range(min//2, 2, -1):
        cach_1 += 1
        if max % i == 0 and min % i == 0:
            ucln = i
            break
print("Uoc chung lon nhat: ",ucln)
print(f'So lan lap cach 1: {cach_1}')

#Cach 2

def hcfnaive(a, b):

    if (b == 0):
        return a
    else:
        return hcfnaive(b, a % b)

# prints 12
print("The gcd of 60 and 48 is : ", end="")
print(hcfnaive(a, b))


#Cach 3
cach_3 = 0
def computeGCD(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):

        if ((x % i == 0) and (y % i == 0)):
            gcd = i

    return gcd

# prints 12
print("The gcd of 60 and 48 is : ", end="")
print(computeGCD(a, b))


cach_4 = 0
#Cach 4 Using Euclidean Algorithm
def computeGCD(x, y):
    while (y):

        x, y = y, x % y

    return x

# prints 12
print("The gcd of 60 and 48 is : ", end="")
print(computeGCD(a, b))


#Cach 5 Using gcd() can compute the same gcd with just one line.
"""
math.gcd( x, y )
Parameters : 
x :  Non-negative integer whose gcd has to be computed.
y : Non-negative integer whose gcd has to be computed.
Return Value : 
This method will return an absolute/positive integer value after 
calculating the GCD of given parameters x and y.
Exceptions : 
When Both x and y are 0, function returns 0, If any number is a character ,
Type error is raised.
"""
import math

# prints 12
print("The gcd of 60 and 48 is : ", end="")
print(math.gcd(a, b))

"""
Trên giang hồ còn 1 cách nữa: Xét cặp số a , b . Điều kiện lặp là a != b
Nếu a > b thì: a  = a - b
Nếu b < a thì: b = b - a
Nếu a == b thì: dừng vòng lặp kết quả in ra ucln là a hay b cũng như nhau vì hcungs bằng nhau
a = 4 ; b = 6
đầu tiên a khác b và ta thấy b > a
=> b = b - a 
=> b = 6 - 4 = 2
lúc này a = 2 & b = 4 ta lại thấy b > a 
=> b = b - a 
=> b = 4 - 2 = 2
lúc này a == b == 2 => ucln = 2
"""