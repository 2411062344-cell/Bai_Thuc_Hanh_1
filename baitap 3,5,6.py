Ten = "nguyen van A" 
Diem_toan = 8.5
Diem_van =7.0
So_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000
print("ho va ten hoc sinh:",Ten)
print("diem mon toan:",Diem_toan)
print("diem mon van:",Diem_van)
print("so luong mon hoc da dang ky:",So_luong_mon_hoc)
print("muc luong toi thieu quy dinh :",MUC_LUONG_TOI_THIEU)

a = 17
b = 5
print(" a + b", a + b)
print(" a - b", a - b)
print(" a * b", a * b)
print(" a / b", a / b)
print(" a // b", a // b)
print(" a % b", a % b)
print(" a ** b", a ** b)
print()
diem = 6.5
tuoi = 20
check_diem = ( diem >= 6.5) and (diem<= 8.0)
print("diem dat loai kha ?:",check_diem)
check_tuoi =(tuoi<= 18)or(tuoi >= 60)
print ("tuoi chua du 18 hoac tren 60?:",check_tuoi )
print("phu dinh dieu kien tuoi:", not check_tuoi)

x = 10 
x += 5
print(" sau khi += 5, x =",x)
x -= 5
print("Sau khi -= 5, x =", x)

x *= 5
print("Sau khi *= 5, x =", x)

x /= 5
print("Sau khi /= 5, x =", x)

x //= 5
print("Sau khi //= 5, x =", x)

x **= 5
print("Sau khi **= 5, x =", x)

danh_sach = [1, 2, 3, "python"]
print("So 3 co trong danh sach khong?:", 3 in danh_sach)

list1 = danh_sach
list2 = [1, 2, 3, "python"]
print("list1 is danh_sach?:", list1 is danh_sach)
print("list2 is danh_sach?:", list2 is danh_sach)


print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(10 > 5 and 3 < 1 or not False)

bien = 10
print(bien, type(bien))
bien = "Xin chao"
print(bien, type(bien))
bien = 3.14
print(bien, type(bien))
bien = True
print(bien, type(bien))


ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

# Tính điểm trung bình
dtb = (diem_toan + diem_ly + diem_hoa) / 3

# Các biểu thức logic kiểm tra điều kiện xếp loại
la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

# In kết quả ra màn hình (Nhớ viết thẳng hàng lề trái)
print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?:", la_gioi)
print("Dat loai Kha?:", la_kha)
print("Dat loai Trung binh?:", la_trung_binh)
print("Dat loai Yeu?:", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))
