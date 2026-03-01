import tkinter as tk   #ПРИ НАЖАТИИ НА ЧЕТНЫЕ ЦВЕТ МЕНЯЮЮТ

# --- главное окно ---
root = tk.Tk()
root.title("Главное меню")
root.geometry("300x200")


def open_second_window():
    # создаём новое окно
    second = tk.Toplevel()
    second.title("Большое меню")
    second.geometry("400x300")

    # большая надпись
    tk.Label(
        second, 
        text="Выберите вариант с четными числами и посмотрите что будет", 
        font=("Arial", 20)
    ).pack(pady=20)


    def make_green(btn):
        btn.config(bg="green")

    def make_yellow(btn):
        btn.config(bg="yellow")

    # кнопки
    tk.Button(second, text="Вариант 1", font=("Arial", 16), width=15).pack(pady=5)
     #команда ламбда позволяет создаёт “мини-функцию”, которую Tkinter вызовет позже — при клике.

    btn2 = tk.Button(second, text="Вариант 2", font=("Arial", 16), width=15,
                     command=lambda: make_green(btn2))
    btn2.pack(pady=5)

    tk.Button(second, text="Вариант 3", font=("Arial", 16), width=15).pack(pady=5)

    btn4 = tk.Button(second, text="Вариант 4", font=("Arial", 16), width=15,
                     command=lambda: make_yellow(btn4))
    btn4.pack(pady=5)

    tk.Button(second, text="Закрыть", font=("Arial", 14), command=second.destroy).pack(pady=20)


tk.Button(root, text="Открыть большое меню",
          font=("Arial", 16), command=open_second_window).pack(pady=50)

root.mainloop()