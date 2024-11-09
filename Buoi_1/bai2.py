import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, integrate


# Hàm kiểm tra cú pháp hàm số
def is_valid_expression(expr):
  try:
    x = symbols('x')
    eval(expr)
    return True
  except Exception:
    return False


# Hàm giải phương trình
def solve_equation():
  equation_str = entry_equation.get()
  x = symbols('x')

  if not is_valid_expression(equation_str):
    messagebox.showerror("Lỗi", "Cú pháp phương trình không hợp lệ!")
    return

  try:
    eq = Eq(eval(equation_str), 0)
    solutions = solve(eq, x)
    messagebox.showinfo("Kết quả", f"Các nghiệm của phương trình là: {solutions}")
  except Exception as e:
    messagebox.showerror("Lỗi", f"Không thể giải phương trình. Lỗi: {e}")


# Hàm vẽ đồ thị
def plot_function():
  func_str = entry_function.get()
  x_range = entry_range.get().split(',')

  if not is_valid_expression(func_str):
    messagebox.showerror("Lỗi", "Cú pháp hàm số không hợp lệ!")
    return

  try:
    x_min = float(x_range[0])
    x_max = float(x_range[1])
    x = np.linspace(x_min, x_max, 100)
    y = eval(func_str)

    plt.figure()
    plt.plot(x, y)
    plt.title(f'Đồ thị của {func_str}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.show()
  except Exception as e:
    messagebox.showerror("Lỗi", f"Không thể vẽ đồ thị. Lỗi: {e}")


# Hàm tính tích phân
def calculate_integral():
  func_str = entry_integral_function.get()
  x = symbols('x')

  if not is_valid_expression(func_str):
    messagebox.showerror("Lỗi", "Cú pháp hàm số không hợp lệ!")
    return

  try:
    lower_limit = float(entry_lower_limit.get())
    upper_limit = float(entry_upper_limit.get())
    integral_value = integrate(eval(func_str), (x, lower_limit, upper_limit))
    messagebox.showinfo("Kết quả Tích Phân",
                        f"Tích phân của {func_str} từ {lower_limit} đến {upper_limit} là: {integral_value}")
  except Exception as e:
    messagebox.showerror("Lỗi", f"Không thể tính tích phân. Lỗi: {e}")


# Tạo giao diện người dùng
app = tk.Tk()
app.title("Ứng dụng Giải Tích")

# Khung cho giải phương trình
frame_equation = tk.Frame(app)
frame_equation.pack(pady=10)

label_equation = tk.Label(frame_equation, text="Nhập phương trình (vd: x**2 - 4):")
label_equation.pack()
entry_equation = tk.Entry(frame_equation)
entry_equation.pack()
button_solve = tk.Button(frame_equation, text="Giải phương trình", command=solve_equation)
button_solve.pack()

# Khung cho vẽ đồ thị
frame_function = tk.Frame(app)
frame_function.pack(pady=10)

label_function = tk.Label(frame_function, text="Nhập hàm số (vd: x**2):")
label_function.pack()
entry_function = tk.Entry(frame_function)
entry_function.pack()
label_range = tk.Label(frame_function, text="Nhập khoảng (vd: -10,10):")
label_range.pack()
entry_range = tk.Entry(frame_function)
entry_range.pack()
button_plot = tk.Button(frame_function, text="Vẽ đồ thị", command=plot_function)
button_plot.pack()

# Khung cho tính tích phân
frame_integral = tk.Frame(app)
frame_integral.pack(pady=10)

label_integral_function = tk.Label(frame_integral, text="Nhập hàm số để tích phân (vd: x**2):")
label_integral_function.pack()
entry_integral_function = tk.Entry(frame_integral)
entry_integral_function.pack()
label_lower_limit = tk.Label(frame_integral, text="Nhập giới hạn dưới:")
label_lower_limit.pack()
entry_lower_limit = tk.Entry(frame_integral)
entry_lower_limit.pack()
label_upper_limit = tk.Label(frame_integral, text="Nhập giới hạn trên:")
label_upper_limit.pack()
entry_upper_limit = tk.Entry(frame_integral)
entry_upper_limit.pack()
button_integrate = tk.Button(frame_integral, text="Tính Tích Phân", command=calculate_integral)
button_integrate.pack()

# Chạy ứng dụng
app.mainloop()