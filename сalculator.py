import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_profit():
    try:
        start_balance = float(entry_start.get())
        end_balance = float(entry_end.get())

        if start_balance <= 0:
            raise ValueError("Начальный баланс должен быть больше нуля.")

        profit = end_balance - start_balance
        percent = (profit / start_balance) * 100

        result_text = f"Прибыль: ${profit:.2f}\nПроцент к депозиту: {percent:.2f}%"
        label_result.config(text=result_text)

        save_to_history(start_balance, end_balance, profit, percent)

    except ValueError as e:
        messagebox.showerror("Ошибка ввода", f"Пожалуйста, введите корректные числа.\n{e}")

def save_to_history(start, end, profit, percent):
    with open("history.txt", "a", encoding="utf-8") as f:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(
            f"[{time_now}] Начальный баланс: ${start:.2f}, Конечный: ${end:.2f}, "
            f"Прибыль: ${profit:.2f}, Процент: {percent:.2f}%\n"
        )

# Интерфейс
root = tk.Tk()
root.title("Калькулятор прибыли")
root.geometry("300x220")
root.resizable(False, False)

tk.Label(root, text="Начальный баланс ($):").pack(pady=(10, 0))
entry_start = tk.Entry(root)
entry_start.pack()

tk.Label(root, text="Конечный баланс ($):").pack(pady=(10, 0))
entry_end = tk.Entry(root)
entry_end.pack()

tk.Button(root, text="Рассчитать", command=calculate_profit).pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
