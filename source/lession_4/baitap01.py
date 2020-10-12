#Bài 01: Viết chương trình tính tổng, tích của các phần tử trong một list.
#Python arithmetic Operators
#Example 1
my_list = [1, 2, 3]
sum = 0
multi = 1
for i in my_list:
    sum += i
    multi *= i
print(f"Sum of all elements in given list 1: {sum} \tTich la: {multi}")

#Example 2
#create a list
list = [5,3,78,55,25]
total = 0
multip = 1
# Iterate each element in list
# and add them in variale total
for l in range(0,len(list)):
    total = total + list[l]
    multip = multip * list[l]

print(f'Sum of all elements in given list 2: {total} & Multip {multip}')

#Example 3
list = [45,23,7,3,2]
sumof = 0
mulof = 1
ele = 0
while ele < len(list):
    sumof = sumof + list[ele]
    mulof = mulof * list[ele]
    ele += 1
print(f'Sum of all elements in given list 3: {sumof} & Multip {mulof}')
