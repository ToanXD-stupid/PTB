# x, y, z = 10, 6 ,8
# a = x < 12 and z > 16
# b = x > 15 or y < 8
# c = not b
# print("a:", a, "\n")
# print("b:", b)
# print("c:", c)

# theodebai = int(input("Nhập số bất kì "))
# if (theodebai % 2 ==0) :
#     print(theodebai, "là số chẵn")
# elif(theodebai % 2 >=1):
#     print(theodebai,"là số lẻ")
# else:
#     print("Ko có nghĩa")

n = int(input("Nhập số dương bất kì: "))
if (n < 0):
    n = n *(-1)
    print ("Trị tuyệt đối của n à", n)
else : 
    print(n)