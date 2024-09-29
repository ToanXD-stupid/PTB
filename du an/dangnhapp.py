sau = input("nhap sau: ")
def a(sau):
    for i in range(1, len(sau) + 1):
        print(sau[:i])

a(sau)      
def tinh_diem_trung_binh(diem_so):
    if len(diem_so) == 0:
        return 0.0
    
    tong_diem = sum(diem_so[:-1]) + diem_so[-1] * 2
    so_diem = len(diem_so) + 1  
    
    diem_trung_binh = tong_diem / so_diem
    return round(diem_trung_binh, 1)
def main():
    diem_an = input("Nhập các điểm của An (cách nhau bởi dấu cách): ").split()
    diem_an = [float(diem) for diem in diem_an]
    
    diem_tb = tinh_diem_trung_binh(diem_an)
    print(f"Điểm trung bình môn Tin học của An là: {diem_tb}")
if __name__ == "__main__":
    main()
