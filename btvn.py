import tkinter as tk
import pandas as pd

root = tk.Tk()
root.title("thông tin nhân viên")

tk.Label(root, text="Mã:").grid(row=0, column=0)
ma = tk.Entry(root)
ma.grid(row=0, column=1)

tk.Label(root, text="Tên:").grid(row=1, column=0)
ten = tk.Entry(root)
ten.grid(row=1, column=1)

tk.Label(root, text="Đơn vị:").grid(row=2, column=0)
donvi = tk.Entry(root)
donvi.grid(row=2, column=1)

tk.Label(root, text="Chức danh:").grid(row=3, column=0)
chucdanh = tk.StringVar(value="Thường")
tk.Radiobutton(root, text="Thường", variable=chucdanh, value="Thường").grid(row=3, column=1)
tk.Radiobutton(root, text="Lớp phó", variable=chucdanh, value="Lớp phó").grid(row=3, column=2)
tk.Radiobutton(root, text="Lớp trưởng", variable=chucdanh, value="Lớp trưởng").grid(row=3, column=3)

tk.Label(root, text="Ngày sinh (DD/MM/YYYY):").grid(row=4, column=0)
ngaysinh = tk.Entry(root)
ngaysinh.grid(row=4, column=1)

tk.Label(root, text="Giới tính:").grid(row=5, column=0)
gioitinh = tk.StringVar(value="Nam")
tk.Radiobutton(root, text="Nam", variable=gioitinh, value="Nam").grid(row=5, column=1)
tk.Radiobutton(root, text="Nữ", variable=gioitinh, value="Nữ").grid(row=5, column=2)

tk.Label(root, text="Số CCCD:").grid(row=6, column=0)
cccd = tk.Entry(root)
cccd.grid(row=6, column=1)

tk.Label(root, text="Ngày cấp:").grid(row=7, column=0)
ngaycap = tk.Entry(root)
ngaycap.grid(row=7, column=1)

tk.Label(root, text="Nơi cấp:").grid(row=8, column=0)
noicap = tk.Entry(root)
noicap.grid(row=8, column=1)
def csv():
    data = {
        "Mã": [ma.get()],
        "Tên": [ten.get()],
        "Đơn vị": [donvi.get()],
        "Chức danh": [chucdanh.get()],
        "Ngày sinh": [ngaysinh.get()],
        "Giới tính": [gioitinh.get()],
        "Số CMND": [cccd.get()],
        "Ngày cấp": [ngaycap.get()],
        "Nơi cấp": [noicap.get()]
    }
    df = pd.DataFrame(data)
    df.to_csv("inforNV",index=False)


tk.Button(root, text="Lưu",command=csv).grid(row=9, column=1)
tk.Button(root, text="Sinh nhật hôm nay").grid(row=10, column=1)
tk.Button(root, text="Xuất danh sách").grid(row=11, column=1)

root.mainloop()
