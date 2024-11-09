import numpy as np
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext

def load_data(file_path):
    """Load data from a CSV file into a numpy array."""
    try:
        data = np.genfromtxt(file_path, delimiter=',', dtype=str, encoding='utf-8', skip_header=1)
        if data.size == 0:
            raise ValueError("File is empty or improperly formatted.")
        return data
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found. Please check the file path.")
        return np.array([])
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
        return np.array([])
    except Exception as e:
        print(f"Error loading data: {e}")
        messagebox.showerror("Error", "An unexpected error occurred while loading data.")
        return np.array([])

def search_student(data, student_id):
    """Search for a student's information by ID."""
    if data.size == 0:
        return "Dữ liệu không được tải."

    student_data = data[data[:, 0] == student_id]
    if student_data.size == 0:
        return f"Không tìm thấy thông tin cho sinh viên có ID {student_id}."
    else:
        return "\n".join([", ".join(row) for row in student_data])

def search_subject(data, subject_name):
    """Search for grades of a specific subject."""
    if data.size == 0:
        return "Dữ liệu không được tải."

    subject_data = data[data[:, 2] == subject_name]
    if subject_data.size == 0:
        return f"Không tìm thấy điểm cho môn học {subject_name}."
    else:
        return "\n".join([f"ID: {row[0]}, Tên: {row[1]}, Điểm: {row[3]}" for row in subject_data])

def calculate_average(data, student_id):
    """Calculate the average grade for a specific student using numpy."""
    if data.size == 0:
        return "Dữ liệu không được tải."

    student_data = data[data[:, 0] == student_id]
    if student_data.size == 0:
        return f"Không tìm thấy thông tin cho sinh viên có ID {student_id}."
    else:
        try:
            grades = student_data[:, 3].astype(float)  # Convert grades to float
            average_grade = np.mean(grades)
            return f"Trung bình cộng điểm của sinh viên có ID {student_id} là {average_grade:.2f}."
        except ValueError:
            return "Có lỗi khi chuyển đổi điểm sang số thực. Vui lòng kiểm tra dữ liệu."

def search_action():
    choice = choice_var.get()
    student_id = id_entry.get().strip()
    subject_name = subject_entry.get().strip()

    if choice == '1':  # Tìm kiếm thông tin sinh viên
        result = search_student(data, student_id)
    elif choice == '2':  # Tìm kiếm điểm môn học
        result = search_subject(data, subject_name)
    elif choice == '3':  # Tính TBC điểm của sinh viên
        result = calculate_average(data, student_id)
    else:
        result = "Lựa chọn không hợp lệ."

    # Hiển thị kết quả trong Text widget
    result_text.delete(1.0, tk.END)  # Xóa nội dung cũ
    result_text.insert(tk.END, result)  # Chèn kết quả mới

def main():
    global data
    file_path = 'data.csv'  # Đặt đường dẫn đến file dữ liệu của bạn
    data = load_data(file_path)

    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Tìm kiếm thông tin sinh viên")

    # Thiết lập màu sắc và kiểu chữ
    root.configure(bg='#f0f0f0')

    # Thêm các widget
    tk.Label(root, text="Chọn hành động:", bg='#f0f0f0', font=('Arial', 14)).pack(pady=10)

    global choice_var
    choice_var = tk.StringVar(value='1')

    tk.Radiobutton(root, text="Tìm kiếm thông tin sinh viên", variable=choice_var, value='1', bg='#f0f0f0', font=('Arial', 12)).pack(anchor='w', padx=20)
    tk.Radiobutton(root, text="Tìm kiếm điểm môn học", variable=choice_var, value='2', bg='#f0f0f0', font=('Arial', 12)).pack(anchor='w', padx=20)
    tk.Radiobutton(root, text="Tính TBC điểm của sinh viên", variable=choice_var, value='3', bg='#f0f0f0', font=('Arial', 12)).pack(anchor='w', padx=20)

    tk.Label(root, text="ID sinh viên:", bg='#f0f0f0', font=('Arial', 12)).pack(pady=5)
    global id_entry
    id_entry = tk.Entry(root, font=('Arial', 12))
    id_entry.pack(pady=5, padx=20)

    tk.Label(root, text="Tên môn học (nếu có):", bg='#f0f0f0', font=('Arial', 12)).pack(pady=5)
    global subject_entry
    subject_entry = tk.Entry(root, font=('Arial', 12))
    subject_entry.pack(pady=5, padx=20)

    tk.Button(root, text="Tìm kiếm", command=search_action, bg='#4CAF50', fg='white', font=('Arial', 12)).pack(pady=20)

    # Thêm Text widget để hiển thị kết quả
    global result_text
    result_text = scrolledtext.ScrolledText(root, width=50, height=10, font=('Arial', 12), wrap=tk.WORD)
    result_text.pack(pady=10, padx=20)

    root.mainloop()

if __name__ == "__main__":
    main()