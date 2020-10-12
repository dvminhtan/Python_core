""""
Viết chương trinh hiển thị đồng hồ điện tử bấm giây theo quy tắc như sau. Ban dâudf
sẽ để là 00:00(phút:giấy)
Khi nhấn enter lập tức tăng số giây lên và khi giây tăng đến 59 thì lúc này phút sẽ tăng lên 1 và giấy se reset về 00
đang chạy bấm phím pause (phím cách)thì tạm dừng lại

-Làm sao để mà khi nhấn phím space nó dừng lại, khi nhấn lần nữa nó sẽ chạy tiếp
- Bấm phím ESC để dừng hản lại
=> dùng cơ hiệu đầu tiên set cho nó là 0 => chay, khi nào nhấn phím space thi set cho nó là 1 => dừng,
nhấn thêm nữa thì lại set về 0 là chạy
hoặc là biến dem = 0, mỗi lần nhấp space là dem++
nếu dem là số lẻ => chạy
nếu dem là số chẵn = > dừng
- Làm sao nó hiểu ta đang nhấn phím space?
Cách 1  char x = getch();
Cách 2 nên dùng hàm bắt phím sau:

"""