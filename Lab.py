import tkinter as tk
from math import sin, cos, tan, pi

def calculate(operation):
    try:
        value = float(entry.get())
        
        if operation == "sin":
            result = sin(value)
        elif operation == "cos":
            result = cos(value)
        elif operation == "tg":
            result = tan(value)
        elif operation == "ctg":
            result = 1 / tan(value) if tan(value) != 0 else "Undefined"
        else:
            result = "Error"
        
        result_label.config(text=f"Результат: {result}")
    except Exception as e:
        result_label.config(text=f"Помилка: {str(e)}")

# Головне вікно
root = tk.Tk()
root.title("Тригонометричний калькулятор")
root.geometry("400x200")

# Ввід
entry_label = tk.Label(root, text="Введіть число:")
entry_label.pack()
entry = tk.Entry(root, width=30)
entry.pack()

# Кнопки операцій
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

operations = ["sin", "cos", "tg", "ctg"]
for operation in operations:
    btn = tk.Button(button_frame, text=operation, width=10, 
                    command=lambda op=operation: calculate(op))
    btn.pack(side=tk.LEFT, padx=5, pady=5)

# Виведення результату
result_label = tk.Label(root, text="Результат: ", font=("Arial", 12))
result_label.pack(pady=10)

# Запуск програми
root.mainloop()
