import tkinter as tk   #СЕГОДНЯ ПРОБУЮ СЧЕТ КНОПОК ПО НОЖАТИЮ

root = tk.Tk()
root.title("Счётчик кликов")
root.geometry("300x150")

count = 0  #переменная счётчика

def plus_one():
    global count
    count += 1
    label.config(text=f"Счётчик: {count}")

#надпись
label = tk.Label(root, text="Счётчик: 0", font=("Arial", 16))
label.pack(pady=10)

#кнопка
button = tk.Button(root, text="Нажми меня", font=("Arial", 14), command=plus_one)
button.pack()

root.mainloop()