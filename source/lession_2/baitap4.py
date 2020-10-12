"""
Bài 4. Lập trình thực hiện các công việc sau:
    Nhập 3 số a, b, c bất kì
    Hãy kiểm tra xem ba số đó có phải là độ dài của các cạnh của một tam giác hay không?
    Nếu đúng là tam giác thì xác định là tam giác vuông hay không?
    Gợi ý: Điều kiện để tạo thành 1 tam giác đó là tổng của 2 cạnh bất kỳ luôn lớn hơn cạnh còn lại.
"""
a = float(input("Nhap vao canh 1: "))
b = float(input("Nhap vao canh 2: "))
c = float(input("Nhap vao canh 3: "))
#trường hợp không hợp lệ
if a + b <= c and a + c > b and b + c > a:
    print("Ba canh khong tao thanh tam giac.")
"""
xử lý: Đưa trường hợp đặc biệt lên đầu
1.Đều - 2. Vuông cân --- 3. Vuông ---- 4. Cân --- 5. Thường
"""
if a == b and b ==c:
    print("Tam giac deu.")
#Cân
if a == b or a == c or b == c:
    #Vuông
    if a * a + b * b == c * c or a * a + c == b * b or b * b + c * c == a * a:
        print("Tam giac vuong can.")
    print("Tam giac can")
print("Tam giac thuong.")