import tkinter as tk
from tkinter import ttk

def on_button_click():
    try:
        # اجرای محاسبات بر اساس مقادیر وارد شده
        result = eval(entry.get())
        # نمایش نتیجه در برچسب
        label_result.config(text=f"Result: {result}")
    except Exception as e:
        # در صورت وجود خطا، نمایش پیام خطا
        label_result.config(text="Error")

def on_digit_click(digit):
    # افزودن عدد به محتوای ورودی
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(digit))

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("ماشین حساب مهندسی")

# ایجاد ویجت‌ها
entry = ttk.Entry(root, width=30, font=('Arial', 14))
label_result = ttk.Label(root, text="Result: ")

# ایجاد دکمه‌های محیط گرافیکی برای اعداد
for digit in range(10):
    button_digit = ttk.Button(root, text=str(digit), command=lambda d=digit: on_digit_click(d))
    button_digit.grid(row=(9 - digit) // 3 + 2, column=(digit % 3) + 1, padx=5, pady=5)

# دکمه مساوی
button_equals = ttk.Button(root, text="=", command=on_button_click)
button_equals.grid(row=5, column=3, padx=5, pady=5)

# دکمه‌های عملگرها
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button_operator = ttk.Button(root, text=operator, command=lambda op=operator: on_digit_click(op))
    button_operator.grid(row=i+2, column=4, padx=5, pady=5)

# پیکربندی ویجت‌ها در پنجره
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
label_result.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# مشاهده پنجره
root.mainloop()
