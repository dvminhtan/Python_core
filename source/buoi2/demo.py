"""
- Kiểu dữ liệu boolean chỉ có 2 giá trị: True - Đúng, False - Sai
- Các phép toán trên kiểu dữ liệu boolean:
    Phép toán           Ý nghĩa
    not x               Phủ định của x. True nếu x False và ngược lại
    x and y             Kiểm tra điều kiện đồng thời. True nếu cả x và y đều True, nếu không thì False
    x or y              Kiểm tra có 1 trong 2 điều kiện đúng. False nếu cả x và y đều False, nếu không thì True
- Bảng giá trị chân lý cho các phép toán:
    x           y           not x           x and y         x or y
    True        True        False           True            True
    True        False       False           False           True
    False       True        True            False           True
    False       False       True            False           False
"""

# Nhập chương trình sau và chạy thử để kiểm tra kết quả
# a = True  
# b = False
# print(a + 9)
# print(b + 9)
# print('not a is:', not a)
# print('not b is:', not b)
# print('a or b is:', a or b)
# print('a and b is:', a and b)

""" Các phép toán so sánh:
    Phép toán           Ý nghĩa
        ==              So sánh bằng. True nếu 2 bên bằng nhau
        !=              So sánh khác (không bằng). True nếu 2 bên khác nhau
        >               So sánh lớn hơn. True nếu bên trái lớn hơn bên phải
        >=              So sánh lớn hơn hoặc bằng. True nếu bên trái lớn hơn hoặc bằng bên phải
        <               So sánh nhỏ hơn. True nếu bên trái nhỏ hơn bên phải
        <=              So sánh nhỏ hơn hoặc bằng. True nếu bên trái nhỏ hơn hoặc bằng bên phải
"""

# x = 2000
# y = 3000
# print('x == y is', x == y)
# print('x != y is', x != y)
# print('x > y is', x > y)
# print('x < y is', x < y)
# print('x >= y is', x >= y)
# print('x <= y is', x <= y)

""" Các cú pháp tắt cho cho việc cập nhật giá trị
        Cú pháp ngắn        Cú pháp đầy đủ
        n += 1              n = n + 1
        n -= 2              n = n - 2
        n *= 3              n = n * 3
        n /= x              n = n / x
        n **= 4             n = n ** 4
        a %= b              a = a % b
"""

""" Cú pháp cho vòng for
    for i in sequence:
        các câu lệnh sẽ chạy của mỗi vòng lặp
"""
# Ví dụ: In ra cá giá trị nguyên từ 0 đến 9
# for i in range(10):
#     print(i)

""" Hàm range(start=0, stop, step_size=1): Generate a sequence of numbers
    + start: giá trị bắt đầu sinh.
    + stop: giá trị kết thúc sinh, có nghĩa là sinh đến giá trị bé hơn stop. Không có mặc định
    + step_size: bước nhảy để sinh các giá trị tiếp theo từ start (nhận cả giá trị âm và dương)
"""
#Lệnh này có chạy hay không?
# for i in range (1,0,1):
#     print("Tân đẹp trai")

# Ví dụ: In ra cá giá trị nguyên chẵn có một chữ số- Giá trị là bao nhiêu ?
# for i in range(0, 10, 2):
#     print(i, end=" ")

# For loop from 0 to 2, therefore running 3 times.
# for x in range(0, 3):
#     print("We're on time %d" % (x))

""" Chương trình: Nhập vào 2 số nguyên, in ra màn hình:
    + Tổng của 2 số đó, nếu cả 2 số đều dương
    + Tích của 2 số đó nếu cả 2 số đều âm
    + Nếu không thì vui lòng in ra màn hình số nhỏ hơn trong 2 số đó
"""
 i = 1
 while i < 10:
     print(i)
     i += 1
     if i == 5:
         break