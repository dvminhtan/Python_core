'''
Bài 10: Viết hàm đếm số lần xuất hiện các từ đơn trong một đoạn văn bản
'''
my_string = "Hello i'm minh tan"
 
    # break the string into list of words 
str_list = my_string.split() 
  
    # gives set of unique words 
unique_words = set(str_list) 
      
for words in unique_words : 
    print('Frequency of ', words , 'is :', str_list.count(words))