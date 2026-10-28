ho_ten = input("nhap ho ten:")
nam_sinh = int(input("nhap nam sinh:"))
diem_tb = float(input("nhap diem trung binh:"))
print("ho ten:", ho_ten)
print("nam sinh:", nam_sinh)
print("diem trung binh:", diem_tb)


print("python", "la", "mot", "ngon", "ngu", "lap", "trinh", sep="\n")
print("dong 1", end="|")
print("dong 2")


# f-string
print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} -DTB: {diem_tb:.2f}")

# str.format()
print("Ho ten: {0} - Nam sinh: {1} - DTB: {2:.2f}".format(ho_ten, nam_sinh, diem_tb))

# toan tu %
print("Ho ten: %s - Nam sinh: %d - DTB: %.2f" % ( ho_ten, nam_sinh, diem_tb))

    # Chu thich mot dong: khai bao thong tin sinh vien
"""
Chu thich/docstring nhieu dong:
Chuong trinh quan ly diem sinh vien - Buoi 2
"""
ho_ten = "Tran Thi B" # bien luu ho ten
nam_sinh = 2000 # bien luu nam sinh
diem_tb = 8.5 # bien luu diem trung binh


s1 = 'Xin chao'
s2 = "Ban co khoe khong?"
s3 = '''Day la
mot chuoi
nhieu dong'''
s4 = "Duong dan: C:\\Python\\data"
s5 = r"Duong dan raw: C:\Python\data"
s6 = "Toi ten la \"Nam\", con ban ten gi?"
print(s1); print(s2); print(s3); print(s4); print(s5); print(s6)