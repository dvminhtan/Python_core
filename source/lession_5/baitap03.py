#Bài 03: Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu tuple.
'''
Algorithm
Step 1: Given a list.
Step 2: Use one counter variable c which is initialized by 0.
Step 3: We traverse the list and verify that encountering a tuple or not in our path of count.
Step 4: If it’s true then counter will be increased by 1 otherwise false.
Step 5: return c
'''
my_list = ['hi', 'hello',(1,2,3),176]
count = 0
for i in my_list:
    if isinstance(i,tuple):
        break
    count += 1
print(count)