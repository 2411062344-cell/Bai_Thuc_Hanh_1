import sqlite3

TEN_FILE_CSDL = "chi_tieu.db"

def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS giao_dich (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_khoan TEXT NOT NULL,
            so_tien REAL NOT NULL,
            loai TEXT NOT NULL,
            danh_muc TEXT NOT NULL,
            ngay_thang TEXT NOT NULL
        )
    """)
    ket_noi.commit()
    ket_noi.close()

def them_giao_dich(ten_khoan, so_tien, loai, danh_muc, ngay_thang):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "INSERT INTO giao_dich (ten_khoan, so_tien, loai, danh_muc, ngay_thang) VALUES (?, ?, ?, ?, ?)",
        (ten_khoan, so_tien, loai, danh_muc, ngay_thang)
    )
    ket_noi.commit()
    ket_noi.close()

def lay_toan_bo_giao_dich():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT id, ten_khoan, so_tien, loai, danh_muc, ngay_thang FROM giao_dich ORDER BY id DESC")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def xoa_giao_dich(id_gd):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM giao_dich WHERE id = ?", (id_gd,))
    ket_noi.commit()
    ket_noi.close()

def thong_ke_theo_danh_muc():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    # Thống kê tổng tiền theo các danh mục chi tiêu
    con_tro.execute("SELECT danh_muc, SUM(so_tien) FROM giao_dich WHERE loai = 'Chi' GROUP BY danh_muc")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua