import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import csdl_chi_tieu as db
from datetime import datetime

DANH_SACH_DANH_MUC = ["An uong", "Nha o", "Giai tri", "Di lai", "Luong", "Khac"]

class UngDungChiTieu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly Chi tieu ca nhan")
        self.geometry("620x500")
        self.resizable(False, False)
        
        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()

    def khoi_tao_giao_dien(self):
        # Khung nhập liệu
        khung_nhap = tk.LabelFrame(self, text=" Thong tin giao dich ", padx=10, pady=10)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Ten khoan:").grid(row=0, column=0, sticky="w", pady=5)
        self.o_ten = tk.Entry(khung_nhap, width=25)
        self.o_ten.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(khung_nhap, text="So tien:").grid(row=0, column=2, sticky="w", pady=5)
        self.o_tien = tk.Entry(khung_nhap, width=15)
        self.o_tien.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(khung_nhap, text="Loai:").grid(row=1, column=0, sticky="w", pady=5)
        self.chon_loai = ttk.Combobox(khung_nhap, values=["Thu", "Chi"], width=23, state="readonly")
        self.chon_loai.current(1)
        self.chon_loai.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(khung_nhap, text="Danh muc:").grid(row=1, column=2, sticky="w", pady=5)
        self.chon_danh_muc = ttk.Combobox(khung_nhap, values=DANH_SACH_DANH_MUC, width=13, state="readonly")
        self.chon_danh_muc.current(0)
        self.chon_danh_muc.grid(row=1, column=3, padx=5, pady=5)

        tk.Button(khung_nhap, text="Them giao dich", bg="lightgreen", command=self.xu_ly_them).grid(row=2, column=0, columnspan=4, pady=10)

        # Khung hiển thị danh sách giao dịch
        khung_ds = tk.Frame(self)
        khung_ds.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox = tk.Listbox(khung_ds, width=80, height=12)
        self.listbox.pack(side="left", fill="both", expand=True)

        thanh_cuon = tk.Scrollbar(khung_ds, orient="vertical", command=self.listbox.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=thanh_cuon.set)

        # Khung nút chức năng thao tác
        khung_nut = tk.Frame(self)
        khung_nut.pack(pady=10)

        tk.Button(khung_nut, text="Xoa giao dich chon", bg="lightcoral", command=self.xu_ly_xoa).grid(row=0, column=0, padx=10)
        tk.Button(khung_nut, text="Bieu do chi tieu (Matplotlib)", bg="lightblue", command=self.xu_ly_thong_ke).grid(row=0, column=1, padx=10)

    def tai_lai_danh_sach(self):
        self.listbox.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_giao_dich()
        for gd in self.danh_sach_hien_tai:
            id_gd, ten, tien, loai, dm, ngay = gd
            dau = "+" if loai == "Thu" else "-"
            self.listbox.insert(tk.END, f"[{loai}] {ten} : {dau}{tien:,.0f} VND ({dm}) - Ngày: {ngay}")

    def xu_ly_them(self):
        ten = self.o_ten.get().strip()
        s_tien = self.o_tien.get().strip()
        loai = self.chon_loai.get()
        danh_muc = self.chon_danh_muc.get()
        ngay = datetime.now().strftime("%Y-%m-%d")

        if not ten or not s_tien:
            messagebox.showerror("Loi", "Vui long nhap day du ten va so tien.")
            return
        
        try:
            tien = float(s_tien)
            if tien <= 0:
                raise ValueError()
        except ValueError:
            messagebox.showerror("Loi", "So tien phai la mot so duong hop le.")
            return

        db.them_giao_dich(ten, tien, loai, danh_muc, ngay)
        self.o_ten.delete(0, tk.END)
        self.o_tien.delete(0, tk.END)
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thanh cong", "Da them giao dich moi.")

    def xu_ly_xoa(self):
        lua_chon = self.listbox.curselection()
        if not lua_chon:
            messagebox.showerror("Loi", "Vui long chon mot giao dich de xoa.")
            return
        
        id_gd = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.xoa_giao_dich(id_gd)
        self.tai_lai_danh_sach()

    def xu_ly_thong_ke(self):
        du_lieu = db.thong_ke_theo_danh_muc()
        if not du_lieu:
            messagebox.showinfo("Thong bao", "Chua co du lieu chi tieu de thong ke.")
            return

        danh_muc = [row[0] for row in du_lieu]
        tong_tien = [row[1] for row in du_lieu]

        # Vẽ biểu đồ tròn thể hiện tỷ trọng chi tiêu
        plt.figure(figsize=(6, 6))
        plt.pie(tong_tien, labels=danh_muc, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
        plt.title("Ty le chi tieu theo danh muc")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    app = UngDungChiTieu()
    app.mainloop()