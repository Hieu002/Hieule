import numpy as np
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def solve_equations(A, B):
    try:
        A_inv = np.linalg.inv(A)
        X = np.dot(A_inv, B)
        return X
    except np.linalg.LinAlgError:
        return None

def calculate():
    try:
        n = int(entry_n.get())
        A = np.zeros((n, n))
        B = np.zeros(n)

        for i in range(n):
            for j in range(n):
                A[i][j] = float(entry_A[i][j].get().replace(',', '.'))
            B[i] = float(entry_B[i].get().replace(',', '.'))

        X = solve_equations(A, B)
        if X is not None:
            X_rounded = [round(x, 5) for x in X]
            result = "Nghiệm của hệ phương trình:\n" + "\n".join([f"x[{i+1}] = {X_rounded[i]}" for i in range(n)])
            messagebox.showinfo("Kết quả", result)
        else:
            messagebox.showerror("Lỗi", "Hệ phương trình không có nghiệm hoặc có vô số nghiệm.")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số. Hãy chắc chắn rằng bạn nhập số thực (ví dụ: -3,14 hoặc 2,5).")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")

def create_entries():
    try:
        n = int(entry_n.get())
        for widget in frame_A.winfo_children():
            widget.destroy()

        for i in range(n):
            row_entries = []
            for j in range(n):
                hint = chr(97 + j) if i == 0 else f"{chr(97 + j)}{i+1}"
                entry = tk.Entry(frame_A, width=10)
                entry.grid(row=i, column=j, padx=5, pady=5, sticky=tk.W + tk.E)
                entry.insert(0, hint)
                entry.bind("<FocusIn>", lambda e: clear_hint(e.widget))
                row_entries.append(entry)
            entry_A.append(row_entries)

            hint_b = f"a{i+1}"
            entry_b = tk.Entry(frame_A, width=10)
            entry_b.grid(row=i, column=n, padx=5, pady=5, sticky=tk.W + tk.E)
            entry_b.insert(0, hint_b)
            entry_b.bind("<FocusIn>", lambda e: clear_hint(e.widget))
            entry_B.append(entry_b)

        for j in range(n + 1):
            frame_A.grid_columnconfigure(j, weight=1)

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên cho n.")

def clear_hint(entry):
    if entry.get() in [f"{chr(97 + j)}{entry.grid_info()['row'] + 1}" if entry.grid_info()['row'] > 0 else chr(97 + j) for j in range(entry.grid_info()['column'] + 1)] or entry.get() in [f"a{i+1}" for i in range(len(entry_B))]:
        entry.delete(0, tk.END)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Giải hệ phương trình")

# Cấu hình nền
background_image = Image.open("hinh1.png")  # Đường dẫn đến hình ảnh nền
background_image = background_image.resize((800, 600), Image.LANCZOS)  # Thay đổi kích thước hình ảnh
bg_image = ImageTk.PhotoImage(background_image)

# Label để hiển thị hình nền
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Đặt vị trí và kích thước cho Label

# Nhập số lượng phương trình
tk.Label(root, text="Nhập số lượng phương trình (n):", bg="lightblue").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
entry_n = tk.Entry(root, width=10)
entry_n.grid(row=0, column=1, padx=5, pady=5)

# Nút để tạo các trường nhập
tk.Button(root, text="Tạo trường nhập", command=create_entries).grid(row=0, column=2, padx=5, pady=5)

# Khung cho ma trận A
frame_A = tk.Frame(root, bg="lightblue")  # Đặt màu nền cho khung
frame_A.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

entry_A = []
entry_B = []

# Cấu hình cho phép mở rộng
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Nút tính toán
tk.Button(root, text="Tính toán", command=calculate).grid(row=2, column=0, columnspan=3, pady=10)

# Hướng dẫn cho người dùng
tk.Label(root, text="Nhập số thực với dấu phẩy cho số thập phân và dấu '-' cho số âm.", bg="lightblue").grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Bắt đầu vòng lặp chính
try:
    root.mainloop()
except KeyboardInterrupt:
    print("Chương trình đã dừng.")