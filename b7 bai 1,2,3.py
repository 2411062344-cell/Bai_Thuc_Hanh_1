tuoi = int(input("Nhap tuoi: "))
print("Tuoi cua ban la:", tuoi)
try:
  tuoi = int(input("Nhap tuoi: "))
  print("Tuoi cua ban la:", tuoi)
except ValueError:
      print("Ban da nhap sai dinh dang, vui long nhap mot so nguyen.")

while True:
    try:
        so_luong = int(input("Nhap so luong (so nguyen duong): "))
        if so_luong > 0:
         break
        print("So luong phai lon hon 0, vui long nhap lai.")

    except ValueError:
        print("Du lieu khong hop le, vui long nhap lai mot so nguyen.")
        print("So luong hop le da nhap:", so_luong)