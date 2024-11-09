import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt


# Hàm tính toán diện tích và chu vi
def calculate():
  shape = shape_var.get()
  try:
    if shape == "Tam giác":
      base = float(entry_base.get())
      height = float(entry_height.get())
      side1 = float(entry_side1.get())
      side2 = float(entry_side2.get())
      side3 = float(entry_side3.get())
      area = 0.5 * base * height
      perimeter = side1 + side2 + side3
      result_text.set(f"Diện tích: {area:.2f}\nChu vi: {perimeter:.2f}")
      draw_triangle(base, height)

    elif shape == "Hình chữ nhật":
      length = float(entry_length.get())
      width = float(entry_width.get())
      area = length * width
      perimeter = 2 * (length + width)
      result_text.set(f"Diện tích: {area:.2f}\nChu vi: {perimeter:.2f}")
      draw_rectangle(length, width)

    elif shape == "Hình tròn":
      radius = float(entry_radius.get())
      area = np.pi * (radius ** 2)
      perimeter = 2 * np.pi * radius
      result_text.set(f"Diện tích: {area:.2f}\nChu vi: {perimeter:.2f}")
      draw_circle(radius)

    elif shape == "Hình thang":
      base1 = float(entry_base1.get())
      base2 = float(entry_base2.get())
      height = float(entry_height_trapezoid.get())
      side1 = float(entry_side1_trapezoid.get())
      side2 = float(entry_side2_trapezoid.get())
      area = 0.5 * (base1 + base2) * height
      perimeter = base1 + base2 + side1 + side2
      result_text.set(f"Diện tích: {area:.2f}\nChu vi: {perimeter:.2f}")
      draw_trapezoid(base1, base2, height)

    elif shape == "Hình trụ":
      radius = float(entry_cylinder_radius.get())
      height = float(entry_cylinder_height.get())
      volume = np.pi * (radius ** 2) * height
      surface_area = 2 * np.pi * radius * (height + radius)
      result_text.set(f"Thể tích: {volume:.2f}\nDiện tích bề mặt: {surface_area:.2f}")
      draw_cylinder(radius, height)

    elif shape == "Hình nón":
      radius = float(entry_cone_radius.get())
      height = float(entry_cone_height.get())
      slant_height = float(entry_cone_slant_height.get())
      volume = (1 / 3) * np.pi * (radius ** 2) * height
      surface_area = np.pi * radius * (radius + slant_height)
      result_text.set(f"Thể tích: {volume:.2f}\nDiện tích bề mặt: {surface_area:.2f}")
      draw_cone(radius, height, slant_height)

    elif shape == "Cầu":
      radius = float(entry_sphere_radius.get())
      volume = (4 / 3) * np.pi * (radius ** 3)
      surface_area = 4 * np.pi * (radius ** 2)
      result_text.set(f"Thể tích: {volume:.2f}\nDiện tích bề mặt: {surface_area:.2f}")
      draw_sphere(radius)

  except ValueError:
    messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số.")


# Hàm vẽ hình
def draw_triangle(base, height):
  plt.figure()
  plt.fill([0, base, base / 2], [0, 0, height], 'b', alpha=0.5)
  plt.xlim(-1, base + 1)
  plt.ylim(-1, height + 1)
  plt.title("Tam giác")
  plt.xlabel("Chiều rộng")
  plt.ylabel("Chiều cao")
  plt.grid()
  plt.show()


def draw_rectangle(length, width):
  plt.figure()
  plt.fill([0, length, length, 0], [0, 0, width, width], 'g', alpha=0.5)
  plt.xlim(-1, length + 1)
  plt.ylim(-1, width + 1)
  plt.title("Hình chữ nhật")
  plt.xlabel("Chiều dài")
  plt.ylabel("Chiều rộng")
  plt.grid()
  plt.show()


def draw_circle(radius):
  theta = np.linspace(0, 2 * np.pi, 100)
  x = radius * np.cos(theta)
  y = radius * np.sin(theta)
  plt.figure()
  plt.fill(x, y, 'r', alpha=0.5)
  plt.xlim(-radius - 1, radius + 1)
  plt.ylim(-radius - 1, radius + 1)
  plt.title("Hình tròn")
  plt.xlabel("Bán kính")
  plt.ylabel("Bán kính")
  plt.grid()
  plt.gca().set_aspect('equal')
  plt.show()


def draw_trapezoid(base1, base2, height):
  plt.figure()
  plt.fill([0, base1, base2, 0], [0, 0, height, height], 'y', alpha=0.5)
  plt.xlim(-1, max(base1, base2) + 1)
  plt.ylim(-1, height + 1)
  plt.title("Hình thang")
  plt.xlabel("Chiều dài")
  plt.ylabel("Chiều cao")
  plt.grid()
  plt.show()


def draw_cylinder(radius, height):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  z = np.linspace(0, height, 100)
  theta = np.linspace(0, 2 * np.pi, 100)
  theta_grid, z_grid = np.meshgrid(theta, z)
  x_grid = radius * np.cos(theta_grid)
  y_grid = radius * np.sin(theta_grid)
  ax.plot_surface(x_grid, y_grid, z_grid, alpha=0.5)
  ax.set_title("Hình trụ")
  plt.show()


def draw_cone(radius, height, slant_height):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  z = np.linspace(0, height, 100)
  theta = np.linspace(0, 2 * np.pi, 100)
  theta_grid, z_grid = np.meshgrid(theta, z)
  x_grid = radius * (height - z_grid) / height * np.cos(theta_grid)
  y_grid = radius * (height - z_grid) / height * np.sin(theta_grid)
  ax.plot_surface(x_grid, y_grid, z_grid, alpha=0.5)
  ax.set_title("Hình nón")
  plt.show()


def draw_sphere(radius):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  u = np.linspace(0, 2 * np.pi, 100)
  v = np.linspace(0, np.pi, 100)
  x = radius * np.outer(np.cos(u), np.sin(v))
  y = radius * np.outer(np.sin(u), np.sin(v))
  z = radius * np.outer(np.ones(np.size(u)), np.cos(v))
  ax.plot_surface(x, y, z, color='b', alpha=0.5)
  ax.set_title("Cầu")
  plt.show()


# Khởi tạo ứng dụng
app = tk.Tk()
app.title("Ứng Dụng Tính Toán Hình Học")
app.geometry("400x600")
app.config(bg="#e0f7fa")  # Màu nền nhẹ nhàng

shape_var = tk.StringVar(value="Tam giác")

# Chọn hình học
tk.Label(app, text="Chọn hình:", bg="#e0f7fa", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
shape_menu = tk.OptionMenu(app, shape_var, "Tam giác", "Hình chữ nhật", "Hình tròn", "Hình thang", "Hình trụ",
                           "Hình nón", "Cầu")
shape_menu.grid(row=0, column=1, padx=10, pady=5)

# Nhập dữ liệu
entry_base = tk.Entry(app)
entry_height = tk.Entry(app)
entry_side1 = tk.Entry(app)
entry_side2 = tk.Entry(app)
entry_side3 = tk.Entry(app)

entry_length = tk.Entry(app)
entry_width = tk.Entry(app)

entry_radius = tk.Entry(app)

entry_base1 = tk.Entry(app)
entry_base2 = tk.Entry(app)
entry_height_trapezoid = tk.Entry(app)
entry_side1_trapezoid = tk.Entry(app)
entry_side2_trapezoid = tk.Entry(app)

entry_cylinder_radius = tk.Entry(app)
entry_cylinder_height = tk.Entry(app)

entry_cone_radius = tk.Entry(app)
entry_cone_height = tk.Entry(app)
entry_cone_slant_height = tk.Entry(app)

entry_sphere_radius = tk.Entry(app)

result_text = tk.StringVar()
tk.Label(app, textvariable=result_text, bg="#e0f7fa", font=("Arial", 12)).grid(row=8, column=0, columnspan=2, padx=10,
                                                                               pady=10)


def show_entries():
  # Ẩn tất cả widget nhập liệu
  for widget in app.grid_slaves():
    if int(widget.grid_info()["row"]) > 1 and int(widget.grid_info()["row"]) < 8:
      widget.grid_forget()

  # Hiển thị trường nhập liệu tương ứng
  if shape_var.get() == "Tam giác":
    tk.Label(app, text="Cạnh đáy:").grid(row=1, column=0)
    entry_base.grid(row=1, column=1)
    tk.Label(app, text="Chiều cao:").grid(row=2, column=0)
    entry_height.grid(row=2, column=1)
    tk.Label(app, text="Cạnh 1:").grid(row=3, column=0)
    entry_side1.grid(row=3, column=1)
    tk.Label(app, text="Cạnh 2:").grid(row=4, column=0)
    entry_side2.grid(row=4, column=1)
    tk.Label(app, text="Cạnh 3:").grid(row=5, column=0)
    entry_side3.grid(row=5, column=1)

  elif shape_var.get() == "Hình chữ nhật":
    tk.Label(app, text="Chiều dài:").grid(row=1, column=0)
    entry_length.grid(row=1, column=1)
    tk.Label(app, text="Chiều rộng:").grid(row=2, column=0)
    entry_width.grid(row=2, column=1)

  elif shape_var.get() == "Hình tròn":
    tk.Label(app, text="Bán kính:").grid(row=1, column=0)
    entry_radius.grid(row=1, column=1)

  elif shape_var.get() == "Hình thang":
    tk.Label(app, text="Cạnh đáy 1:").grid(row=1, column=0)
    entry_base1.grid(row=1, column=1)
    tk.Label(app, text="Cạnh đáy 2:").grid(row=2, column=0)
    entry_base2.grid(row=2, column=1)
    tk.Label(app, text="Chiều cao:").grid(row=3, column=0)
    entry_height_trapezoid.grid(row=3, column=1)
    tk.Label(app, text="Cạnh bên 1:").grid(row=4, column=0)
    entry_side1_trapezoid.grid(row=4, column=1)
    tk.Label(app, text="Cạnh bên 2:").grid(row=5, column=0)
    entry_side2_trapezoid.grid(row=5, column=1)

  elif shape_var.get() == "Hình trụ":
    tk.Label(app, text="Bán kính:").grid(row=1, column=0)
    entry_cylinder_radius.grid(row=1, column=1)
    tk.Label(app, text="Chiều cao:").grid(row=2, column=0)
    entry_cylinder_height.grid(row=2, column=1)

  elif shape_var.get() == "Hình nón":
    tk.Label(app, text="Bán kính:").grid(row=1, column=0)
    entry_cone_radius.grid(row=1, column=1)
    tk.Label(app, text="Chiều cao:").grid(row=2, column=0)
    entry_cone_height.grid(row=2, column=1)
    tk.Label(app, text="Chiều cao nghiêng:").grid(row=3, column=0)
    entry_cone_slant_height.grid(row=3, column=1)

  elif shape_var.get() == "Cầu":
    tk.Label(app, text="Bán kính:").grid(row=1, column=0)
    entry_sphere_radius.grid(row=1, column=1)

  tk.Button(app, text="Tính toán", command=calculate, bg="#4CAF50", fg="white").grid(row=7, column=0, columnspan=2,
                                                                                     pady=10)


shape_var.trace("w", lambda *args: show_entries())

show_entries()  # Hiển thị trường nhập đầu tiên

app.mainloop()