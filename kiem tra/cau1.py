a =[5, 12, 15, 7, 7, 30, 3, 56]
sum = 0
for i in range(len(a)):
    print(a[i])
    if a[i] % 2 ==0:
        sum += a[i]

print("Tổng số chắn trong danh sách là :",sum)