so_KWh_tieu_thu = int(input("Nhập số điện tiêu thụ trong tháng: "))
so_tien_tra = 0
if so_KWh_tieu_thu <= 50:
    so_tien_tra += so_KWh_tieu_thu * 1700
elif 51 >= so_KWh_tieu_thu <= 100:
    so_tien_tra = (50*1700) + (so_KWh_tieu_thu - 50 * 1900)
elif 101 >= so_KWh_tieu_thu <= 200:
    so_tien_tra = (50*1700) + (50 * 1900) + (so_KWh_tieu_thu - 100 * 2100)
elif so_KWh_tieu_thu > 200:
    so_tien_tra = (50*1700) + (50 * 1900) + (100 * 2100) +(so_KWh_tieu_thu - 200)*3000
print(so_tien_tra)