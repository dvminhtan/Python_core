'''
Bài 07: Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu theo tập các key cho trước
Ví dụ:
    dict ban đầu: sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
    keys = ["name", "salary"]
    Output: {'name': 'Kelly', 'salary': 8000}
'''
my_dict = {'a': 100, 'b':200, 'c':300}
new_dict = {}
keys = ['a','b']

for key in my_dict:
    if key in keys:
        new_dict.update({key: my_dict.get(key)})
print(new_dict)