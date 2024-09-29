sotientieu_thu2 = int(input("Số tiền chi tiêu trong thứ 2: "))
sotientieu_thu3 = int(input("Số tiền chi tiêu trong thứ 3: "))
sotientieu_thu4 = int(input("Số tiền chi tiêu trong thứ 4: "))
sotientieu_thu5 = int(input("Số tiền chi tiêu trong thứ 5: "))
sotientieu_thu6 = int(input("Số tiền chi tiêu trong thứ 6: "))
sotientieu_thu7 = int(input("Số tiền chi tiêu trong thứ 7: "))
tong = sotientieu_thu2 + sotientieu_thu3 + sotientieu_thu4 + sotientieu_thu5 + sotientieu_thu6 + sotientieu_thu7
print("Tổng số tiền chi tiêu trong tuần: ",tong ,"đồng")
trungbinh = (tong)%7
print("Số tiền tiêu trung bình trong tuần là: ",trungbinh)