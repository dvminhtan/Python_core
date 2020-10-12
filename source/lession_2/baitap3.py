# Bài 3. Lập chương trình thực hiện các công việc sau:
#     Nhập 1 số nguyên dương n bất kì (n<1000). Yêu cầu kiểm tra dữ liệu đầu vào, nếu sai yêu cầu nhập lại.
#     Tính tổng các chữ số của số đó.
#     Hiển thị kết qủa ra màn hình

while True:
    n = int(input("Nhap vao n: "))
    if n >= 1000:
        print("Gia tri n < 1000. Xin vui long nhap lai")
        break
    else:
        sum = 0
        for i in range(1, n + 1):
            print(i, end=" ")
            sum += i

print('\nTong la: %d' % sum)
