import tkinter as tk
from calculator import calculate

def calculate_and_display(operation):
    try:
        value = float(entry.get())
        result = calculate(operation, value)
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Введіть дійсне число")

# Графічний інтерфейс
root = tk.Tk()
root.title("Тригонометричний калькулятор")
root.geometry("1000x200")

# Ввід
entry_label = tk.Label(root, text="Введіть число:")
entry_label.pack()
entry = tk.Entry(root, width=30)
entry.pack()

# Кнопки операцій
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

operations = ["sin", "cos", "tg", "ctg", "arcsin", "arccos", "arctg", "arcctg"]
for operation in operations:
    btn = tk.Button(button_frame, text=operation, width=10, 
                    command=lambda op=operation: calculate_and_display(op))
    btn.pack(side=tk.LEFT, padx=5, pady=5)

# Виведення результату
result_label = tk.Label(root, text="Результат: ", font=("Arial", 12))
result_label.pack(pady=10)

# Запуск програми
root.mainloop()
