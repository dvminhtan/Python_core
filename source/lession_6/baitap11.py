'''
Bài 11: Viết chương trình để sinh ra dict mới từ list các dict có dạng như trong ví dụ:
Ví dụ:
    Input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
    Output: {'item1': 1150, 'item2': 300}
'''

while True:
    print("Nhập 1 số nguyên:", end=" ")
    n = int(input())
    if n > 0:
        print("Đã nhập số dương. Chương trình đã dừng lại!")
        break
    print("Đã nhập số âm. Chương trình sẽ tiếp tục!")

print(f"Gia tri n la: {n}")