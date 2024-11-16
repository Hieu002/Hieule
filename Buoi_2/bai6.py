import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error


class StudentPerformanceApp:
  def __init__(self, master):
    self.master = master
    self.master.title("Dự đoán hiệu quả học tập của sinh viên")

    self.data = None
    self.model = None

    # Load Data
    tk.Button(master, text="Load Data", command=self.load_data).grid(row=0, column=0)

    # Train Model
    tk.Button(master, text="Train", command=self.train_model).grid(row=1, column=0)

    tk.Label(master, text="Chọn thuật toán:").grid(row=1, column=1)
    self.algorithm_var = tk.StringVar(value='KNN')
    tk.OptionMenu(master, self.algorithm_var, 'KNN', 'Decision Tree', 'SVM', 'Linear Regression').grid(row=1, column=2)

    # Test Model
    tk.Button(master, text="Test", command=self.test_model).grid(row=2, column=0)

    # Input New Data
    tk.Label(master, text="Số giờ học:").grid(row=3, column=0)
    self.entry_hours_studied = tk.Entry(master)
    self.entry_hours_studied.grid(row=3, column=1)

    tk.Label(master, text="Điểm số trước đó:").grid(row=4, column=0)
    self.entry_previous_scores = tk.Entry(master)
    self.entry_previous_scores.grid(row=4, column=1)

    tk.Label(master, text="Hoạt động ngoại khóa (0/1):").grid(row=5, column=0)
    self.entry_extracurricular_activities = tk.Entry(master)
    self.entry_extracurricular_activities.grid(row=5, column=1)

    tk.Label(master, text="Số giờ ngủ:").grid(row=6, column=0)
    self.entry_sleep_hours = tk.Entry(master)
    self.entry_sleep_hours.grid(row=6, column=1)

    tk.Label(master, text="Số đề thi đã luyện tập:").grid(row=7, column=0)
    self.entry_sample_question_papers_practiced = tk.Entry(master)
    self.entry_sample_question_papers_practiced.grid(row=7, column=1)

    tk.Button(master, text="Submit", command=self.predict_performance).grid(row=8, column=0)

    # Kết quả
    self.result_label = tk.Label(master, text="")
    self.result_label.grid(row=9, column=0, columnspan=3)

  def load_data(self):
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
      self.data = pd.read_csv(file_path)
      messagebox.showinfo("Thông báo", "Dữ liệu đã được tải thành công!")

  def train_model(self):
    if self.data is not None:
      X = self.data.drop('Performance Index', axis=1)
      y = self.data['Performance Index']
      X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

      algorithm = self.algorithm_var.get()
      if algorithm == 'KNN':
        self.model = KNeighborsClassifier(n_neighbors=5)
      elif algorithm == 'Linear Regression':
        self.model = LinearRegression()
      # Có thể thêm các thuật toán khác ở đây

      self.model.fit(X_train, y_train)
      messagebox.showinfo("Thông báo", "Mô hình đã được huấn luyện thành công!")
    else:
      messagebox.showerror("Lỗi", "Vui lòng tải dữ liệu trước!")

  def test_model(self):
    if self.model is not None:
        X = self.data.drop('Performance Index', axis=1)
        y = self.data['Performance Index']
        y_pred = self.model.predict(X)
        mse = mean_squared_error(y, y_pred)
        mae = mean_absolute_error(y, y_pred)

        messagebox.showinfo("Kết quả kiểm tra", f"MSE: {mse}\nMAE: {mae}")

        # Vẽ đồ thị
        plt.clf()  # Xóa đồ thị cũ
        plt.scatter(y, y_pred, color='blue', label='Dự đoán')
        plt.xlabel("Giá trị thực")
        plt.ylabel("Giá trị dự đoán")
        plt.title("So sánh giá trị thực và giá trị dự đoán")
        plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linestyle='--', label='Đường tham chiếu')  # Đường tham chiếu
        plt.legend()
        plt.show()
    else:
        messagebox.showerror("Lỗi", "Vui lòng huấn luyện mô hình trước!")

  def predict_performance(self):
    if self.model is not None:
      input_data = pd.DataFrame({'Hours Studied': [float(self.entry_hours_studied.get())],
        'Previous Scores': [float(self.entry_previous_scores.get())],
        'Extracurricular Activities': [int(self.entry_extracurricular_activities.get())],
        'Sleep Hours': [float(self.entry_sleep_hours.get())],
        'Sample Question Papers Practiced': [float(self.entry_sample_question_papers_practiced.get())]})
      prediction = self.model.predict(input_data)
      self.result_label.config(text=f"Dự đoán chỉ số hiệu quả học tập: {prediction[0]}")
    else:
      messagebox.showerror("Lỗi", "Vui lòng huấn luyện mô hình trước!")


if __name__ == "__main__":
  root = tk.Tk()
  app = StudentPerformanceApp(root)
  root.mainloop()