"""
immutable : khổng thể thay đổi được: int, float, decimal, complex frozenset, bôol, bytes
ordered : theo tuần tự
text presentation
mutable: có thể thay đổi đc. adj: list, dict, set, bytearray
"""

"""
my_string = 'Hello world'
#get character by referring to index
#Substrings with slicing
#stringName [startIndex:endIndex]
#Start at index 1 and go until index 5 (not include #5)
sub_string = my_string[1:5]
sub_string = my_string[:5]
sub_string = my_string[6:]
sub_string = my_string[::-1] # reverse the string
sub_string = my_string[::2]# take every second character
print(sub_string)

"""

# concatenate two or more strings: concat strings with +
# greeting = " Hello cac ban"
# channel = "MinhTan"
# sentence = greeting + " Chao mừng các ban đến với  " + channel
# print(sentence)

#join elements of a list into a string: .join()
# my_list = ['How', 'are','you','doing']
# sentence = ' * '.join(my_list)
# print(sentence)

#Iterating
#Iterating over a string by using a for in lôop
# my_string = "Hello Xin chao cac ban"

# for char in my_string:
#     print(char)

# if 'e' in my_string:
#     print("yes")
# else:
#     print("no")

#strip()
#ex: I am alone --> Strips all whitespace character from both ènds
# print("     i am alone   ".strip())
# print("On my school".strip('O'))

#split()
# print('but life is good'.split())
# print('but, is very boring'.split(','))

#replace()
# print('help me'.replace("me","you"))
# my_string = 'need to make a fire'
# print(my_string.startswith('need'))
# print(my_string.endswith('rice'))

my_list = [1, 0, -2]
result = []
for l in my_list:
    result.append(l*l)
print(result)


