'''
Bài 04: Viết hàm
        def is_prime(n)
    để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, nếu có thì trả lại True, nếu không thì trả lại False
'''

# importing sympy module
from sympy import *

print(isprime(13))

#ex2:
def is_prime(num):
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, num):
            if (num % i) == 0:
                # print(num, "is not a prime number")
                return -1
        else:
            # print(num, "is a prime number")
            return 1

    else:
        return -1

n = 17
result = is_prime(n)
if result == 1:
    print("Đây là số nguyên tố")
else:
    print("Đây không phải là số nguyên tố")

#ex3:

def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True
n = 11
result_3 = isPrime(n)

if result_3:
    print("True")
else:
    print("False")