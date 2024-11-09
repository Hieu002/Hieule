import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def process_signal():
  try:
    fs = float(sample_rate_entry.get())  # Tần số lấy mẫu từ người dùng
    if fs <= 0:
      raise ValueError("Tần số lấy mẫu phải lớn hơn 0.")

    t = np.linspace(0, 1, int(fs), endpoint=False)

    # Tần số tín hiệu
    f = float(frequency_entry.get())
    if f <= 0:
      raise ValueError("Tần số tín hiệu phải lớn hơn 0.")

    # Tín hiệu sin
    x = np.sin(2 * np.pi * f * t)
    noise = np.random.normal(0, 0.5, x.shape)  # Thêm nhiễu
    x_noisy = x + noise

    # Lấy kiểu bộ lọc và tần số cắt
    filter_type = filter_option.get()
    cutoff_freq = cutoff_entry.get().strip().split(',')

    # Kiểm tra tần số cắt
    if filter_type == "Band-pass":
      low_cut = float(cutoff_freq[0])
      high_cut = float(cutoff_freq[1])
      if low_cut <= 0 or high_cut <= low_cut:
        raise ValueError("Tần số cắt band-pass không hợp lệ.")
    else:
      cutoff_freq = float(cutoff_freq[0])
      if cutoff_freq <= 0:
        raise ValueError("Tần số cắt phải lớn hơn 0.")

    # Thiết kế bộ lọc
    if filter_type == "Low-pass":
      b, a = signal.butter(3, cutoff_freq / (0.5 * fs))
    elif filter_type == "High-pass":
      b, a = signal.butter(3, cutoff_freq / (0.5 * fs), btype='high')
    elif filter_type == "Band-pass":
      b, a = signal.butter(3, [low_cut / (0.5 * fs), high_cut / (0.5 * fs)], btype='band')
    else:
      messagebox.showerror("Lỗi", "Kiểu bộ lọc không hợp lệ.")
      return

    # Lọc tín hiệu
    x_filtered = signal.filtfilt(b, a, x_noisy)

    # Vẽ đồ thị
    plt.figure(figsize=(12, 10))

    # Đồ thị tín hiệu gốc
    plt.subplot(3, 1, 1)
    plt.plot(t, x, label='Tín hiệu gốc', color='blue', linewidth=2)
    plt.title('Tín hiệu gốc')
    plt.xlabel('Thời gian (s)')
    plt.ylabel('Biên độ')
    plt.grid()
    plt.legend()

    # Đồ thị tín hiệu nhiễu
    plt.subplot(3, 1, 2)
    plt.plot(t, x_noisy, label='Tín hiệu nhiễu', color='orange', linewidth=2)
    plt.title('Tín hiệu nhiễu')
    plt.xlabel('Thời gian (s)')
    plt.ylabel('Biên độ')
    plt.grid()
    plt.legend()

    # Đồ thị tín hiệu sau lọc
    plt.subplot(3, 1, 3)
    plt.plot(t, x_filtered, label='Tín hiệu sau lọc', color='green', linewidth=2)
    plt.title('Tín hiệu sau lọc')
    plt.xlabel('Thời gian (s)')
    plt.ylabel('Biên độ')
    plt.grid()
    plt.legend()

    plt.tight_layout()
    plt.show()

    # Lưu tín hiệu đã lọc vào tệp
    save_filtered_signal(x_filtered, t)

  except ValueError as e:
    messagebox.showerror("Lỗi", str(e))
  except Exception as e:
    messagebox.showerror("Lỗi không xác định", "Đã xảy ra lỗi không xác định. Vui lòng thử lại.")


def save_filtered_signal(filtered_signal, time_vector):
  try:
    filename = filedialog.asksaveasfilename(defaultextension=".csv",
                                            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    if filename:
      np.savetxt(filename, np.column_stack((time_vector, filtered_signal)), delimiter=",", header="Time (s), Amplitude",
                 comments="")
      messagebox.showinfo("Thành công", "Tín hiệu đã được lưu thành công!")
  except Exception as e:
    messagebox.showerror("Lỗi", "Không thể lưu tệp: " + str(e))


# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ứng dụng Xử lý Tín hiệu Số")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Thêm nhãn hướng dẫn
instruction_label = tk.Label(root, text="Nhập tần số tín hiệu và tần số cắt để xử lý tín hiệu.", bg="#f0f0f0",
                             font=("Arial", 10))
instruction_label.pack(pady=(10, 20))

# Nhãn và ô nhập liệu cho tần số lấy mẫu
sample_rate_label = tk.Label(root, text="Nhập tần số lấy mẫu (Hz):", bg="#f0f0f0", font=("Arial", 10))
sample_rate_label.pack()
sample_rate_entry = tk.Entry(root)
sample_rate_entry.pack(pady=(0, 10))

# Nhãn và ô nhập liệu cho tần số
frequency_label = tk.Label(root, text="Nhập tần số tín hiệu (Hz):", bg="#f0f0f0", font=("Arial", 10))
frequency_label.pack()
frequency_entry = tk.Entry(root)
frequency_entry.pack(pady=(0, 10))

# Tùy chọn kiểu bộ lọc
filter_label = tk.Label(root, text="Chọn kiểu bộ lọc:", bg="#f0f0f0", font=("Arial", 10))
filter_label.pack()
filter_option = tk.StringVar(value="Low-pass")
filter_menu = ttk.OptionMenu(root, filter_option, "Low-pass", "Low-pass", "High-pass", "Band-pass")
filter_menu.pack(pady=(0, 10))

# Nhãn và ô nhập liệu cho tần số cắt
cutoff_label = tk.Label(root, text="Nhập tần số cắt (Hz):", bg="#f0f0f0", font=("Arial", 10))
cutoff_label.pack()
cutoff_entry = tk.Entry(root)
cutoff_entry.pack(pady=(0, 20))
cutoff_entry.insert(0, "Nhập tần số cắt cho band-pass (dạng: thấp,cao)")

# Nút để xử lý tín hiệu
process_button = tk.Button(root, text="Xử lý tín hiệu", command=process_signal, bg="#4CAF50", fg="white",
                           font=("Arial", 12))
process_button.pack(pady=(10, 20))

# Chạy ứng dụng
root.mainloop()