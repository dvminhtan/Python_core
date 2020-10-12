
while True:
    print("Nhập 1 số nguyên n:", end=" ")
    n = int(input())
    if n > 0:
        print("Đã nhập số dương. Chương trình đã dừng lại!")
        break
    print("Đã nhập số âm. Chương trình sẽ tiếp tục!")
#
# print(f'Giá trị n là : {n}')
# print(f'Giá trị m là : {m}')



# while True:
#     a = int(input("Nhap a: "))
#     b = int(input("Nhap b: "))
#     try:
#         if a > 0:
#             pass
#             if b > 0:
#                 break
#             print("Nhap sai. Nhap lai")
#             b = int(input("Nhap lai b: "))
#         print("Nhap sai. Nhap lai")
#         a = int(input("Nhap lai a: "))
#         break
#     except ValueError:
#         print("Integer, please")

# print(f'Giá trị a là : {a}')
# print(f'Giá trị b là : {b}')

def func_greet(name='Tan nè', msg='Good morning!'):
    """
    Đây là hàm greet,
    sẽ in ra câu chào hỏi người có tên được truyền vào.
    """
    print(f"Hello {name}. {msg}")

func_greet()
func_greet('Peter')
func_greet('Paul', 'Hôm nay thế nào?!')