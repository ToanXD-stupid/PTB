# a = "Mindx technology"
# print(len(a))
# print(a[0])
# for i in range(len(a)):
#     print(a[i])
# for i in a:
#     print(i)

# s = "abcd123"
# a = "abc"
# b = "d12"
# c = "1234"
# x = a in s
# y = c in s
# print(x)
# print(y)
# xx = s.find(a)
# yy = s.find(b)
# zz = s.find(c)
# print(xx)
# print(yy)
# print(zz)
# xxx = s.find(a, 3, 6)
# print(xxx)


# s = " a b c 1 2 3 4"
# x = s.split()
# print(x)
# st = "1,2,3,4,5,6,7"
# y = st.split(",")
# print(y)

# name = input("Cho bố mày cái tên : ")
# output = name.split()[0]
# print(output)



# s = "Chuc em thi tot"
# a = s.split()
# print(a)

# s = "ab bc cd 123 456 00"
# a = s.find('c')
# print(a)

# s = "0123456789"
# t = " "
# for i in range(len(s)):
#     t = s[i] + t
# print(t)

# Nhập danh sách điểm số từ người dùng
scores = input("Nhập danh sách điểm số, mỗi điểm cách nhau bởi một dấu khoảng trắng: ")

# Chuyển đổi chuỗi điểm số thành danh sách các số nguyên
score_list = list(map(int, scores.split()))

# Kiểm tra xem có điểm 10 trong danh sách hay không
count_10 = score_list.count(10)

# In kết quả
if count_10 > 0:
    print(f"Có {count_10} điểm 10 trong danh sách.")
else:
    print("Bạn chưa có điểm 10.")


