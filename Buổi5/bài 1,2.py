tuoi = 20
if tuoi >= 18:
    print("Da du tuoi truong thanh")
if tuoi >= 18:
       print("Duoc phep dang ky xe may")
else:
       print("Chua du tuoi")
       diem = 7.2
       if diem >= 8.0:
          print("Hoc luc gioi")
       elif diem >= 6.5:
             print("Hoc luc kha")
       elif diem >= 5.0:
             print("Xep loai: Trung binh")
       else:
             print("Xep loai: Yeu")

tuoi = 17
co_giay_phep = False
if tuoi >= 18:
      
  if co_giay_phep:
    print("Duoc phep lai xe")
  else:
     print("Du tuoi nhung chua co giay phep")
else:
 print("Chua du tuoi lai xe")
 ho_ten = "Nguyen Van A"
diem_toan, diem_ly, diem_hoa = 8.0, 7.5, 9.0
dtb = round((diem_toan + diem_ly + diem_hoa) / 3, 2)

if dtb >= 8.0:
  xep_loai = "Gioi"
elif dtb >= 6.5:
  xep_loai = "Kha"
elif dtb >= 5.0:
  xep_loai = "Trung binh"
else:
 xep_loai = "Yeu"

print(f"{ho_ten} - DTB: {dtb} - Xep loai: {xep_loai}")
a = float(input("Nhap so thu nhat: "))
b = float(input("Nhap so thu hai: "))
c = float(input("Nhap so thu ba: "))
if a >= b and a >= c:
  lon_nhat = a
elif b >= a and b >= c:
   lon_nhat = b
else:
  lon_nhat = c
print("So lon nhat la:", lon_nhat)
