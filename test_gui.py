import tkinter as tk

root = tk.Tk()  # Создаём окно
root.title("Пример")
root.geometry("400x200")
root.configure(bg="red")   # фон окна

label = tk.Label(
    root,
    text="Привет",
    fg="yellow",
    bg="red",
    font=("comforta", 20)
)

label.grid(row=0, column=0)

root.mainloop()