
# a = int(input("Nhap a:"))
# b = int(input("Nhap b:"))
# c = int(input("Nhap c:"))
# d = int(input("Nhap d:"))

# def max_min(*numbers):
#     min = numbers[0]
#     max = numbers[0]
#     for number in numbers:
#         if min < number:
#             min = number
#         if max > number:
#             max = number
#     return min,max

# tinh_max,tinh_min = max_min(34,657,34,56,78,45)
# print(tinh_max,tinh_min)
# print(type(tinh_max))
# print(type(tinh_min))

# a_max,a_min = max_min(a,b,c,d)
# print(f"Gia tri lon nhat: {a_max}, Giá trị bé nhất {a_min}")

# print(type(a_max))
# print(type(a_min))

            
# max = None
# while text := input("Nhập số nguyên (Enter để dừng): "):
#     num = int(text)
#     if not max or max < num:
#         max = num

# if max:
#     print("Số lớn nhất đã nhập là", max)

# def say_hello(name):
#     hello_string = "Xin chào "+ name + " "
#     print("=" * (len(hello_string)+2))
#     print("| " + hello_string + " |")
#     print("=" * (len(hello_string)+2))

# a_name = input("Tên của bạn là gì: ")
# say_hello(a_name)

#Tính tuổi
# from datetime import date , datetime
# def calculator_age(year):
#     return date.today().year - year


# get_age = calculator_age(1989)
# print(get_age)

# print("Your date of birth (dd mm yyyy)")
# date_of_birth = datetime.strptime(input("--->"), "%d %m %Y")

# def calculate_age(born):
#     today = date.today()
#     return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

# age = calculate_age(date_of_birth)

# print(age)

# covert_def = lambda f : 5*(f - 32) / 9

# a = int(input("Nhập vào 1 số nguyên: "))
# kq = round(covert_def(a),2)
# print(f"Nhiệt độ là: {kq}")

# def cac_mua(n):
#     if 1 <= n <= 3:
#         return 1
#     elif 4 <= n <= 6:
#         return 2
#     elif 7 <= n <= 9:
#         return 3
#     elif 10 <= n <= 12:
#         return 4
#     else:
#         return -1

# a_cac_mua = int(input("Nhập vào tháng: "))
# result = cac_mua(a_cac_mua)
# if result == 1:
#     print("Đây là mùa Xuân")
# elif result == 2:
#     print("Đây là mùa hạ")
# elif result == 3:
#     print("Đây là mùa thu")
# elif result == 4:
#     print("Đây là mùa Đông")
# else:
#     print("Nhập sai vui lòng nhập lại")

# from math import pi
# # def dien_tich(r):
# #     return pi*r*r

# # a_r = float(input("Nhập vào bán kính: "))
# # result = round(dien_tich(a_r),2)
# # print(f"Diện tích hình tròn là: {result}")

# dien_tich = lambda r : pi*r*r
# chu_vi = float(input("Nhập vào chu vi hình tròn: "))
# print(f"Diện tích hnh tròn là: {round(dien_tich(chu_vi),2)}")

# def dao_chuoi(string_rever):
#     return string_rever[::-1]

# def dao_chuoi(string_rever):
#     return "".join(reversed(string_rever))

# def dao_chuoi(a_string):
#     new_string = ''
#     index = len(a_string)
#     while index:
#         index -= 1                    # index = index - 1
#         new_string += a_string[index] # new_string = new_string + character
#     return new_string

# def dao_chuoi(a_string):
#     new_strings = []
#     index = len(a_string)
#     while index:
#         index -= 1                       
#         new_strings.append(a_string[index])
#     return ''.join(new_strings)

# def dao_chuoi(s): 
#     if len(s) == 1:
#         return s
 
#     return s[-1] + dao_chuoi(s[:-1])

# def dao_chuoi(test):
#     n = len(test)
#     x=""
#     for i in range(n-1,-1,-1):
#         x += test[i]
#     return x

# def dao_chuoi(s):
#     rev = ''
#     for i in reversed(range(len(s))):
#         rev += s[i]
#     return rev

# def dao_chuoi(phrase):
#     reversed = ""
#     length = len(phrase)
#     for i in range(length):
#         reversed += phrase[length-1-i]
#     return reversed
 
# def dao_chuoi(s): return s[0] if len(s)==1 else s[len(s)-1] + dao_chuoi(s[0:len(s)-1])

# def dao_chuoi(text):
#     new_string = []
#     n = len(text)
#     while (n > 0):
#         new_string.append(text[n-1])
#         n -= 1
#     return ''.join(new_string)

# dao_chuoi
# kq = dao_chuoi("minh tân")
# print(kq)

# s = 'Python Core'
# print(s[6])
# print(s[::-2])
# print(s[8:2:-2])
# print(s[::-1])
# print(s[-2::-3])

def finput(n):
    arr=[]
    for i in range(n):
        v = int(input(f"Input item[{i}]: "))
        arr.append(v)
    return arr

# def fsum(arr):
#     sum = 0
#     for i in range(len(arr)):
#         sum += arr[i]
#     return sum

def fsum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

def fmax(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max:
            max = arr[i]
    return max

n = int(input("Nhập số lượng phần tử: "))
arr=finput(n)
print(f"sum = {fsum(arr)}")
print(f"max = {fmax(arr)}")
print(f"avg = {fsum(arr)/len(arr)}")

# a = []
# m = int(input("Nhập số tự nhiên m: "))
# n = int(input("Nhập số tự nhiên n: "))
# for i in range(m):
#     print("Nhập ma trận hàng thứ ",i+1," : ")
#     b = []
#     for j in range(n):
#         x = int(input("Nhập phần tử thứ "+str(j+1)+" : "))
#         b += [x]
#     a.append(b)

# print("Ma trận a đã nhập xong.")
# for i in range(m):
#     for j in range(n):
#         print(a[i][j], end=" ")
#     print()

