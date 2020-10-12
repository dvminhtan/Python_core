"""
Game mini đấm lá kéo
"""
# age = 12
# if age < 12:
#     print("Con nit")
# elif age < 18:
#     print("Tre trau")
#     if age >= 15 and age <= 17:
#         print("Sieu tre trau")
# else:
#     print("Nguoi lon")
#đây là các hàm đã có sẵn khi cài python rồi built-in-- bugs lỗi
from random import randint
print("Nhap: Dam, La Keo: ")
player = input()

computer = randint(0, 2)
#concatenate : Nối
if computer == 0:# comparison statement mênh đề so sánh
    computer = "Dam"# mệnh đề gán assignment statement : mệnh đề giá trị
if computer == 1:
    computer = "La"
if computer == 2:
    computer = "keo"

print("---------")
print("You choose: "+player)
print("Computer chooses: "+computer)

# cach 1
"""
if player == "keo":
    if computer == "Keo":
        print("You Draw")
    if computer == "Dam":
        print("You Lose")
    if computer == "La":
        print("You win")

if player == "Dam":
    if computer == "Keo":
        print("You win")
    if computer == "Dam":
        print("You draw")
    if computer == "La":
        print("You lose")

if player == "La":
    if computer == "Keo":
        print("You lose")
    if computer == "Dam":
        print("You win")
    if computer == "La":
        print("You draw")
"""
#Cach 2 input validation: xử lý đầu vào

if player == computer:
    print("Draw")
else:
    if player == "keo":
        if computer == "Dam":
            print("You Lose")
        else:
            print("You win")

    elif player == "Dam":
        if computer == "Keo":
            print("You win")
        else:
            print("You lose")

    elif player == "La":
        if computer == "Keo":
            print("You lose")
        else:
            print("You win")
    else:
        print("Nhap lai. Nhap sai")