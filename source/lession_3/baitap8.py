'''
3.	Viết hàm tìm xem chuỗi S1 có trong chuỗi S2 hay không? Ví dụ: 
S1 = “viet nam dat nuoc toi yeu”;
S2 =  “dat nuoc”;
Tìm xem chuỗi S2 có xuất hiện trong chuỗi S1 không?
Gợi ý: dùng hàm input yêu cầu người dùng nhập giá trị
-	Xem từ khóa in, not in (kiểm tra chuỗi trong chuỗi)
'''
# def check_2l(str1,str2):
#     return str1 in str2

# if __name__=="__main__":
#     a_str = input("Nhập chuỗi 1: ")
#     b_str = input("Nhập chuỗi 2: ")
#     kq = check_2l(a_str,b_str)
#     if kq:
#         print("Có kí tự chung")
#     else:
#         print("Không có kí tự chung")

def check_2l(str1,str2):
    count = 0
    new_str = ''
    for i in str1:
        for j in str2:
            if i in j and i not in new_str:
                new_str = new_str + i + " "
                count += 1
    return new_str,count

if __name__=="__main__":
    a_str = input("Nhập chuỗi 1: ")
    b_str = input("Nhập chuỗi 2: ")
    kq,count = check_2l(a_str,b_str)
    if count > 0:
        print(f"Có phần tử chung: {kq}")
    else:
        print("Không có phần tử chung")
