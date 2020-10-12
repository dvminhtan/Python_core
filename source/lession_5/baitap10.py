'''
Bài 10: Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
    Viết chương trình để in ra hậu tố (vn, org, net, com) trong các tên miền website trong list trên.
'''
my_list = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]

for i in my_list:
    result = i.rsplit('.', 1)[-1]
    print(result)
