'''
Bài 04: Cho 1 list chứa các tuple không rỗng.
    Viết chương trình sắp xếp list đó theo chiều tăng dần của phần tử cuối trong mỗi tuple.
    Ví dụ: [(2, 5), (4, 1), (0, 0)]  => [(0, 0), (4, 1), (2, 5)]
'''
my_list = [(1, 3), (3, 2), (2, 1)]
new_list = sorted(my_list, key=lambda x: x[-1])
print(new_list)