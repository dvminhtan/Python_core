#Bài 05: Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list.
#Find most frequent element in a list
#Example 1
from collections import Counter
my_list = [ ['red', 'yellow', 'green'], ['red', 'yellow', 'green'], ['red', 'green', 'red']]

new_list = [k for v in my_list for k in v]

c = Counter(new_list)

print (c.most_common(1))

#Example 2
List = [2, 1, 2, 2, 1, 3,7,7,7,7,7,7,7]
def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num

print(most_frequent(List))