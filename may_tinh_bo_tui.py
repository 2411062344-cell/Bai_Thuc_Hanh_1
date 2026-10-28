import tkinter as tk
from tkinter import messagebox

# --- HÀM XỬ LÝ LOGIC ---

def nut_bam(ky_tu):
    """Cập nhật ký tự (số hoặc phép toán) vào màn hình hiển thị"""
    bieu_thuc_hien_tai = bien_bieu_thuc.get()
    bien_bieu_thuc.set(bieu_thuc_hien_tai + str(ky_tu))

def xoa_man_hinh():
    """Xóa toàn bộ biểu thức trên màn hình (Nút C)"""
    bien_bieu_thuc.set("")

def tinh_ket_qua():
    """Xử lý tính toán biểu thức khi nhấn nút '='"""
    try:
        bieu_thuc = bien_bieu_thuc.get()
        # Hàm eval() tự động tính toán chuỗi biểu thức toán học trong Python
        ket_qua = eval(bieu_thuc) 
        bien_bieu_thuc.set(str(ket_qua))
    except ZeroDivisionError:
        messagebox.showerror("Loi", "Khong the chia cho so 0!")
        bien_bieu_thuc.set("")
    except Exception:
        messagebox.showerror("Loi", "Bieu thuc khong hop le!")
        bien_bieu_thuc.set("")


# --- THIẾT KẾ GIAO DIỆN ---

cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("280x350")
cua_so.resizable(False, False)

# Biến lưu trữ văn bản hiển thị trên màn hình máy tính
bien_bieu_thuc = tk.StringVar()

# 1. Ô Entry hiển thị biểu thức và kết quả (Căn lề phải chữ to)
man_hinh = tk.Entry(
    cua_so, 
    textvariable=bien_bieu_thuc, 
    font=("Arial", 18), 
    justify="right", 
    bd=10, 
    insertwidth=4, 
    width=17, 
    borderwidth=5
)
man_hinh.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

# 2. Cấu hình danh sách các nút bấm theo thứ tự (Ký tự, Dòng, Cột)
danh_sach_nut = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# 3. Vòng lặp tự động tạo và sắp xếp các nút bấm lên lưới Grid
for (ky_tu, dong, cot) in danh_sach_nut:
    if ky_tu == '=':
        # Nút tính kết quả
        nut = tk.Button(cua_so, text=ky_tu, font=("Arial", 12, "bold"), width=5, height=2, command=tinh_ket_qua, bg="#4CAF50", fg="white")
    elif ky_tu == 'C':
        # Nút xóa màn hình
        nut = tk.Button(cua_so, text=ky_tu, font=("Arial", 12, "bold"), width=5, height=2, command=xoa_man_hinh, bg="#f44336", fg="white")
    else:
        # Các nút số và phép tính (+ - * /) sử dụng lambda để truyền đúng ký tự được bấm
        nut = tk.Button(cua_so, text=ky_tu, font=("Arial", 12), width=5, height=2, command=lambda x=ky_tu: nut_bam(x))
    
    # Định vị nút trên giao diện
    nut.grid(row=dong, column=cot, padx=4, pady=4)


# Chạy vòng lặp chương trình chính
if __name__ == "__main__":
    cua_so.mainloop()