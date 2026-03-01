import tkinter as tk

# главное окно
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
        text="Выберите вариант", 
        font=("Arial", 20)
    ).pack(pady=20)

    # большие кнопки
    tk.Button(second, text="Вариант 1", font=("Arial", 16), width=15).pack(pady=5)
    tk.Button(second, text="Вариант 2", font=("Arial", 16), width=15).pack(pady=5)
    tk.Button(second, text="Вариант 3", font=("Arial", 16), width=15).pack(pady=5)
    tk.Button(second, text="Вариант 4", font=("Arial", 16), width=15).pack(pady=5)

    # кнопка закрытия окна
    tk.Button(
        second, 
        text="Закрыть", 
        font=("Arial", 14),
        command=second.destroy
    ).pack(pady=20)


# кнопка для перехода
open_btn = tk.Button(
    root, 
    text="Открыть большое меню", 
    font=("Arial", 16), 
    command=open_second_window
)
open_btn.pack(pady=50)

root.mainloop()