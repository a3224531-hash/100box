import tkinter as tk
from tkinter import ttk

def open_game_window():
    main_frame.pack_forget()  # Скрываем главное меню

    game_frame.pack(fill="both", expand=True) 


#главное окно
root = tk.Tk()
root.title("Задача заключённых")
root.geometry("800x600")
root.configure(bg="#f8f9fc")   

#(main_frame)
main_frame = tk.Frame(root, bg="#f8f9fc")
main_frame.pack(fill="both", expand=True)

# Заголовок
title = tk.Label(
    main_frame,
    text="Задача заключённых",
    font=("Arial", 26, "bold"),
    bg="#f8f9fc"
)
title.pack(pady=(30, 5))

# Подзаголовок
subtitle = tk.Label(
    main_frame,
    text="Классическая вероятностная головоломка",
    font=("Arial", 13),
    fg="#666",
    bg="#f8f9fc"
)
subtitle.pack(pady=(0, 20))

# Блок правил (как белая карточка)
rules_box = tk.Frame(main_frame, bg="white", bd=1, relief="solid")
rules_box.pack(pady=10, padx=40, fill="x")

rules_text = tk.Label(
    rules_box,
    text="Правила: Заключённые должны найти свои номера в коробках. "
         "Каждый может открыть половину коробок. "
         "Все должны найти свои номера, чтобы выжить.",
    font=("Arial", 12),
    bg="white",
    justify="left",
    wraplength=700
)
rules_text.pack(padx=15, pady=15)



# Слайдер: Кол-во заключённых

def update_prisoners(val):
    prisoners_value_label.config(text=str(int(float(val))))

label_prisoners = tk.Label(
    main_frame,
    text="Количество заключённых:",
    font=("Arial", 14),
    bg="#f8f9fc"
)
label_prisoners.pack(anchor="w", padx=50)

prisoners_value_label = tk.Label(
    main_frame,
    text="100",
    font=("Arial", 14, "bold"),
    bg="#f8f9fc"
)
prisoners_value_label.pack(anchor="w", padx=320)

prisoners_slider = ttk.Scale(
    main_frame,
    from_=10,
    to=200,
    value=100,
    command=update_prisoners,
    length=700
)
prisoners_slider.pack(padx=40, pady=10)


# Слайдер: Кол-во коробок

def update_boxes(val):
    boxes_value_label.config(text=str(int(float(val))))

label_boxes = tk.Label(
    main_frame,
    text="Количество коробок:",
    font=("Arial", 14),
    bg="#f8f9fc"
)
label_boxes.pack(anchor="w", padx=50)

boxes_value_label = tk.Label(
    main_frame,
    text="100",
    font=("Arial", 14, "bold"),
    bg="#f8f9fc"
)
boxes_value_label.pack(anchor="w", padx=300)

boxes_slider = ttk.Scale(
    main_frame,
    from_=10,
    to=200,
    value=100,
    command=update_boxes,
    length=700
)
boxes_slider.pack(padx=40, pady=10)



# Информация о попытках
attempts_label = tk.Label(
    main_frame,
    text="Попыток на заключённого: 50 (половина от 100 коробок)",
    font=("Arial", 12),
    fg="#333",
    bg="#f8f9fc"
)
attempts_label.pack(pady=10)



# Кнопка — начать игру

start_button = tk.Button(
    main_frame,
    text="▶ Начать игру",
    font=("Arial", 16, "bold"),
    bg="#0c1b33",
    fg="white",
    padx=20,
    pady=10,
    relief="flat",
    command=open_game_window  # ← переход на следующее окно
)
start_button.pack(pady=20)


#                     ОКНО ИГРЫ (game_frame)

game_frame = tk.Frame(root, bg="#e8ecf5")

game_title = tk.Label(
    game_frame,
    text="Игровое окно",
    font=("Arial", 22, "bold"),
    bg="#e8ecf5"
)
game_title.pack(pady=40)

game_frame = tk.Frame(root, bg="#3c009d")  # фиолетовый фон как в макете


# -----------------------------
# Функция генерации коробок
# -----------------------------
def generate_boxes():
    for widget in boxes_frame.winfo_children():
        widget.destroy()

    for i in range(1, 101):
        btn = tk.Button(
            boxes_frame,
            text=str(i),
            font=("Arial", 14, "bold"),
            bg="#ffb300",       # оранжевый
            fg="black",
            width=4,
            height=2,
            relief="flat",
            bd=2
        )
        btn.grid(row=(i - 1) // 10, column=(i - 1) % 10, padx=5, pady=5)


# -----------------------------
# ЛЕВАЯ ЧАСТЬ — 100 коробок
# -----------------------------
boxes_frame = tk.Frame(game_frame, bg="#3c009d")
boxes_frame.place(x=20, y=20)

generate_boxes()  # рисуем 100 кнопок


# -----------------------------
# ПРАВАЯ ПАНЕЛЬ
# -----------------------------
panel = tk.Frame(game_frame, bg="#0043aa")
panel.place(x=550, y=20, width=230, height=560)


# Заголовок
panel_title = tk.Label(
    panel,
    text="Задача 100 заключённых",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#0043aa",
    wraplength=200,
    justify="center"
)
panel_title.pack(pady=10)


# Блок правил (белая карточка)
rules_frame = tk.Frame(panel, bg="white")
rules_frame.pack(pady=10, padx=10, fill="x")

rules_label = tk.Label(
    rules_frame,
    text="Правила:\n100 заключённых должны найти свои номера.\nКаждый открывает до 50 коробок.\nВсе должны найти свои номера, чтобы выжить.",
    font=("Arial", 10),
    bg="white",
    justify="left",
    wraplength=180
)
rules_label.pack(padx=5, pady=5)


# -----------------------------
# БЛОК СТРАТЕГИЙ
# -----------------------------
strat_label = tk.Label(
    panel,
    text="Управление\nСТРАТЕГИЯ",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#0043aa",
    justify="center"
)
strat_label.pack(pady=10)


strategy_var = tk.StringVar(value="random")


btn_random = tk.Radiobutton(
    panel,
    text="Случайная",
    variable=strategy_var,
    value="random",
    font=("Arial", 12),
    bg="#0043aa",
    fg="white",
    activebackground="#0043aa",
    activeforeground="white",
    selectcolor="#0043aa"
)
btn_random.pack(pady=8)

btn_loop = tk.Radiobutton(
    panel,
    text="Петлевая",
    variable=strategy_var,
    value="loop",
    font=("Arial", 12),
    bg="#0043aa",
    fg="white",
    activebackground="#0043aa",
    activeforeground="white",
    selectcolor="#0043aa"
)
btn_loop.pack(pady=9)


# -----------------------------
# Кнопка начать симуляцию
# -----------------------------
start_sim_btn = tk.Button(
    panel,
    text="Начать симуляцию",
    bg="#ff4747",
    fg="white",
    font=("Arial", 14, "bold"),
    relief="flat",
    height=2
)
start_sim_btn.pack(pady=20, padx=10, fill="x")


# -----------------------------
# Статистика (3 белые карточки)
# -----------------------------
def stat_card(parent, title_text):
    frame = tk.Frame(parent, bg="white")
    tk.Label(frame, text=title_text, font=("Arial", 10), bg="white").pack()
    return frame

stat1 = stat_card(panel, "Людей осталось")
stat1.pack(pady=5)

stat2 = stat_card(panel, "Коробок осталось")
stat2.pack(pady=5)

stat3 = stat_card(panel, "Количество попыток")
stat3.pack(pady=5)


# Запускаем окно
root.mainloop()