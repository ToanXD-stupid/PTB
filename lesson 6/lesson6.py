# # i  = 1
# # while True:
# #     print(i)
# #     i += 1

# # for i in range(True):
# #     print(i)

# s = int(input("Nhập một số dương: "))
# if (0 <s< 100):
#     while True:
#         print(s)
#         s += 1
#         if s == 100:
#             break
# else:
#     while s <=0:
#         print("Nhập lại số kh")
#         s = int(input("Nhập một số dương: "))

import random
laptop = random.randint(1,10)
count = 0
while True:
    player = int(input("Nhập số bất kỳ :"))
    count += 1
    if player < laptop:
        print("Số của bản nhỏ hơn")
    elif player > laptop:
        print("Sô của bạn cao hơn")
    else:
        print("Bạn đoán đúng rùi")


    