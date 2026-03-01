import tkinter as tk #переключение цветов по нажатию кнопок,как смена сцен get_tree_change("")

root = tk.Tk()
root.title("Выбор цвета")
root.geometry("300x200")

def change_color(color):
    root.configure(bg=color)
    label.config(text=f"Цвет: {color}", bg=color)

label = tk.Label(root, text="Выбери цвет", font=("Arial", 16))
label.pack(pady=10)

btn_red = tk.Button(root, text="Красный", width=15, command=lambda: change_color("red"))
btn_red.pack(pady=5)

btn_green = tk.Button(root, text="Зелёный", width=15, command=lambda: change_color("green"))
btn_green.pack(pady=5)

btn_blue = tk.Button(root, text="Синий", width=15, command=lambda: change_color("blue"))
btn_blue.pack(pady=5)

root.mainloop()