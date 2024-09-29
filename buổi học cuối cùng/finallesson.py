# def name():
#     print("Nguyen Van A")

# name()
# def tinhtong(a, b):
#     # sum = 0
#     # sum = a + b
#     # return sum
#     return a + b
# print(tinhtong(1, 2))

def gia_tri_tuyet_doi(so):
    if so < 0:
        return -so
    else:
        return so
num = int(input("Nhập số: "))
print(gia_tri_tuyet_doi(num))

def  is_old(num):
    if num % 2 == 0:
        return "Số chẵn"
    else:
        return "Số lẻ"
num = int(input("Nhập số: "))
print(is_old())
print(is_old(2)) # ewewe



