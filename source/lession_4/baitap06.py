"""
Bài 06: Viết chương trình đếm các chuỗi trong một list thỏa mãn:
        + Độ dài từ 2 trở lên
        + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau
"""
# strings = input("Please enter words divided by comma and white space: ")
# x = strings.split()
# y = []
# for i in x:
#     if len(i) > 2:
#         y.append(i) 
#         print(len(y))


test_list = ['python', 'java', 'nan']

# printing list  
print ("The list : " + str(test_list)) 
  
# using naive method  
# to get numbers > k 
count = 0
for i in test_list:
    if len(i) >= 2 and i[0] == i[-1] :
        count += 1
  
# printing the intersection  
print ("The numbers count : " , count)