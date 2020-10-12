#Bài 00: Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc.
#Picking n Random Samples From a List of Elements
import random
#cach 1
items = [1,3,65,78,9,5,34,5,8,56,54]
cach1 = random.sample(items, 3)
print(f'Cach 1: {cach1}')

#cach 2
names = ["Hung","Tan","Nga","Van","Truc","Hieu","Nghia","Nhan"]
print("Random sample with replacement to including repetition")
cach2 = random.choices(names, k=3)
print(f'Cach 2: {cach2}')

#cach 3
print("Create a sampled list of random numbers without duplicates")
cach3 = random.sample(range(100),5)
print(f'Cach 3: {cach3}')