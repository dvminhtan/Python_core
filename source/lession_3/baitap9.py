'''
5.	Giả sử có một chuỗi như sau: “0983876207;75;10:18:25;0918295063”, tách chuỗi trên thành từng phần riêng biệt
Cho biết vị trí thứ 2 trong chuỗi trên là thời gian cuộc gọi từ số thứ 1 “0983876207” sang số thứ 2 “0918295063”. Biết rằng 1 phút cho mỗi cuộc gọi là 2500đ, tính giá cước cuộc gọi trên.
Gợi ý: dùng hàm input yêu cầu người dùng nhập giá trị
-	Dùng hàm split để tách chuỗi 
-	Xác định vị trí thời gian cuộc gọi là vị trí thứ 2
-	Chuyển đổi số trên thành kiểu số (có khả năng tính toán được)
-	2500đ 1 phút thì tính ra 1s là bao nhiều?
-	Sau đó lấy 2 giá trị nhân nhau cho ra kết quả giá tiền của cuộc gọi điện thoại trên.
'''

# def list_string(str):
#     new_str = str.split(";")
#     time = str[2].split(":")
#     total_time = (float(time[0])*60)
#     money = total_time * 2500
#     return money

# if __name__=="__main__":
#     a_string = input("Nhập vào đoạn chuỗi: ")
#     kq = list_string(a_string)
#     print(f"Tổng tiền thanh toán là: {kq}")
def tinh_tien():
    a_string = input("Nhập đoạn chuỗi: ")

    new_str = ''
    new_str = a_string.split(";")
    phone_1 = new_str[0]
    phone_2 = new_str[3]
    time = new_str[2].split(":")

    total = float(time[0])*60 + float(time[1]) + (round(float(time[2])/60,2))
    money = total * 2500
    return money,new_str[0],new_str[3]

tien,phone1,phone2 = tinh_tien()
print(f"Test chương trình: {tien}")
print(f"Test chương trình: {phone1}")
print(f"Test chương trình: {phone2}")
# print(f"Thời gian: {time}")
# print(f"Tổng tiền phải thanh toán: {money}")
