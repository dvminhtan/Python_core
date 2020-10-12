"""
Bài 1. Lập chương trình thực hiện công việc sau:
    Nhập ba số a, b, c bất kì từ bàn phím
    Giải nghiệm phương trình bậc 2: ax^2 + bx + c = 0  (Kể cả trường hợp a=0)
/*
 * b1: Nhập dữ liệu
 * b2: Xử lý
 *  - B2.1: Nếu a = 0 thì phương trình có dạng bx + c = 0
 *      b2.1.1: Nếu b = 0 thì pt có dạng c = 0
 *          b2.1.1.1: Nếu c = 0 thì pt có vô số nghiệm
 *          b2.1.1.2: ngược lại thì phương trình vô nghiệm
 *      +b2.1.2: ngược lại thì x = - c/b
 *   -B2.2: ngược lại: giai bình thường tình delta
         b2.2.1: delta = b * b - 4 * a * c
         b2.2.2: Nếu delta > 0:
            b2.2.2.1: Phương trình có 2 nghiệm phân biệt
                x1 = round((-b + sqrt(delta) / (2 * a)),2)
                x2 = round((-b - sqrt(delta) / (2 * a)),2)
         b2.2.3: Ngược lại nếu delta == 0
            b2.2.3.1: Phương trình có nghiệm kép:
                x = -b / (2 * a)
         b2.2.4: Ngược lại phương trình vô nghiệm
 * b3: in kết quả
 * */
"""
from math import sqrt, pow

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
#Phương trình có dạng bx+c = 0
if a == 0:
    #phương trinh có dạng c = 0
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -c / b
        print("Phương trình có nghiệm x={}".format(x))
else:
    # b ** 2, || b * b
    delta = pow(b,2) - 4 * a * c
    if delta > 0:
        x1 = round((-b + sqrt(delta) / (2 * a)),2)
        x2 = round((-b - sqrt(delta) / (2 * a)),2)
        print("Phương trình có 2 nghiệm phân biệt: x1 ={} , x2 ={}.".format(x1,x2))
    elif delta == 0:
        x = -b / (2 * a)
        print("Phương trình có nghiệm kép x = {}".format(x))
    else:
        print("Phương trinh vô nghiệm")

