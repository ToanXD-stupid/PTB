#  hàm không có giá trị trả về bộ dữ liệu
# def hello():
#     print("hello")
# hello()

# def greeting():
#     full_nam = input("Nhập họ và tên của bạn: ")
#     print("Xin chào ",full_nam)
# greeting()

# def hello(name):
#     print("Xin chào ",name)
# hello("Nguyễn Văn A")
# hello("Nguyễn Văn B")
# hello("Nguyễn Văn C")   

# def full_name(first_name,last_name):
#     print("Xin chào ",first_name,last_name)
#     print("Họ và tên của bạn là: ",first_name,last_name)
# full_name("Nguyễn Văn","A")
# # full_name("Nguyễn Văn","B")
# # full_name("Nguyễn Văn","C")   

# a = 10
# b = 2 
# def tinhlong():
#     print(a + b)
# tinhlong()

def ucln(a, b):
    while b:
        a, b = b, a % b
    return a

def rut_gon_phan_so(tu, mau):
    uoc = ucln(abs(tu), abs(mau))
    return tu // uoc, mau // uoc

def tinh_tong_phan_so(tu1, mau1, tu2, mau2):
    tu = tu1 * mau2 + tu2 * mau1
    mau = mau1 * mau2
    return rut_gon_phan_so(tu, mau)

# Nhập dữ liệu
tu1 = int(input("Nhập tử số của phân số thứ nhất: "))
mau1 = int(input("Nhập mẫu số của phân số thứ nhất: "))
tu2 = int(input("Nhập tử số của phân số thứ hai: "))
mau2 = int(input("Nhập mẫu số của phân số thứ hai: "))

# Tính tổng và rút gọn
tong_tu, tong_mau = tinh_tong_phan_so(tu1, mau1, tu2, mau2)

# Xuất kết quả
print(f"Tổng của {tu1}/{mau1} và {tu2}/{mau2} là: {tong_tu}/{tong_mau}")




