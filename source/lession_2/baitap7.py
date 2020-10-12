"""
Tìm và in lên màn hình tất cả các số nguyên trong phạm vi từ 10 đến 99 sao cho tích của 2 chữ số
bằng 2 lần tổng của 2 chữ số đó. Ví dụ: Số 44
"""
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
while True:
    try:
        if a < 10 or a > 20:
            print("Nhap sai. Nhap lai")
            a = int(input("Nhap lai a: "))
        break
    except ValueError:
        print("Integer, please")
for i in range(a, b + 1):
    hang_chuc = i // 10
    hang_don_vi = i % 10
    if hang_chuc * hang_don_vi == 2 * (hang_chuc + hang_don_vi):
        print(i, end=" ")

"""
Độ phức tạp của thuật toán được dựa trên 2 nguyên tắc.
1. SỐ phép gán 
2. Số phép so sánh
"""