'''
2.	Cho phép người dùng nhập vào một chuỗi. Đổi tất cả ra chữ thường/đổi tất cả ra chữ hoa và xuất ra kết quả ra màn hình
Gợi ý: dùng hàm input yêu cầu người dùng nhập giá trị
-	Nhập chuỗi thư nhất và gán vào biến s
-	Dùng hàm lower đề đổi chuổi thành chữ thường
-	Dùng hàm upper đề đổi chuổi thành chữ HOA
-	Xuất ra màn hình 2 chuổi trên
'''
def convert_char(str):
    new_str = ''
    for i in str:
        if 'a' <= i and i <= 'z':
            new_str = new_str + chr(ord(i) - 32)
        elif 'A' <= i and i <= 'Z':
            new_str = new_str + chr(ord(i) + 32)
        else:
            new_str = new_str + i
    return new_str

if __name__=="__main__":
    a_string = input("Nhập vào 1 chuỗi: ")
    kq = convert_char(a_string)
    print(f"Kết quả nhận được là: {kq}")
