import math
import tkinter as tk
from tkinter import messagebox

def compute_result(x):
    if x < 0.2:
        y = math.sin(x)**2 + math.cos(x**2)
    else:
        y = math.cos(x) + math.exp(math.sqrt(x**2 + 0.1))
    return y

def calculate_result():
    try:
        x = float(entry.get())
        result = compute_result(x)
        messagebox.showinfo("Результат", f"Результат: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Некорректный ввод числового значения x.")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

window = tk.Tk()
window.title("Вычисление значения функции")
window.geometry("300x150")
label = tk.Label(window, text="Введите числовое значение x:")
label.pack()
entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text="Вычислить", command=calculate_result)
button.pack()
window.mainloop()
