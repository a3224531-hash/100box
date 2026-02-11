import customtkinter as ctk

root = ctk.CTk()
root.title("Main page")
root.configure(fg_color="#48088D")
root.geometry("1440x1024")

for i in range(1,101):
    row = (i - 1) // 10
    col = (i - 1) % 10

    hundred =100

    btn = ctk.CTkButton(
        root,
        text = str(i),
        font=("Arial", 37),
        width=80,
        height=80,
        corner_radius=12,
        fg_color="#E5A00B",
        text_color="black",
        hover_color="grey"
    )
    btn.grid(row=row, column=col, padx=6, pady=6)

card = ctk.CTkFrame(
    root,
    width=462,
    height=288,
    corner_radius=20,
    fg_color="#595ABE"
)
card.place(x=950,y=30)

title_label = ctk.CTkLabel(
    card,
    text="Задача 100 заключённых",
    font=("Arial", 20, "bold"),
    text_color="white"
)
title_label.place(x=20, y=20)

desc_label = ctk.CTkLabel(
    card,
    text=(
        "Правила: 100 заключённых должны найти свои номера в 100 коробках."
        " Каждый может открыть до 50 коробок. "
        "Все должны найти свои номера, чтобы выжить."
    ),
    font=("Arial", 16, "bold"),
    text_color="white",
    justify="left",
    wraplength=420
)
desc_label.place(x=20, y=60)
STr_label = ctk.CTkLabel(
    card,
    text=(
        "Стратегии:"
    ),
    font=("Arial", 16, "bold"),
    text_color="white",
    justify="left",
)
STr_label.place(x=20, y=147, anchor = "w")

center_label = ctk.CTkLabel(
    card,
    text=
         "Случайная:\n ~0% успеха. Каждый открывает случайные коробки."
         "\nПетлевая:\n ~31% успеха! Начните с коробки со \nсвоим номером,"
         " затем следуйте цепочке чисел.",
    font=("Arial", 16),
    text_color="white"
)
center_label.place(relx=0.5, rely=0.5,x=10,y=59, anchor="center")
control = ctk.CTkFrame(
    root,
    width=462,
    height=239,
    corner_radius=20,
    fg_color="#E34D4D"
)
control.place(x=950,y=350)
control_label = ctk.CTkLabel(
    control,
    text=(
        "Управление"
    ),
    font=("Arial", 23, "bold"),
    text_color="white",
    justify="left",
)
control_label.place(x=15,y=20, anchor="w")
strateji_label = ctk.CTkLabel(
    control,
    text=(
        "стратегия "
    ),
    font=("Arial", 21, "bold"),
    text_color="white",
    justify="left",
)
strateji_label.place(x=10,y=50, anchor="w")
type_1 = ctk.CTkButton(
    control,
    text="Случайная",
    font=("Arial", 24, "bold"),
    text_color="white",
    fg_color= "#575454",
    corner_radius=20,
    width=210,
)
type_1.place(x=245, y=65, anchor="nw")
type_2 = ctk.CTkButton(
    control,
    text="Петлевая",
    font=("Arial", 24, "bold"),
    text_color="white",
    fg_color= "#575454",
    corner_radius=20,
    width=210,
)
type_2.place(x=245, y=105, anchor="nw")
Start_game = ctk.CTkButton(
    control,
    text="Начать симуляцию ",
    font=("Arial", 24, "bold"),
    text_color="white",
    fg_color= "#575454",
    corner_radius=18,
    width=400,
    height=60
)
Start_game.place(x=245, y=180, anchor="center")


grey_frames = []
for i in range(1,5):
    row = (i - 1) // 2
    col = (i - 1) % 2

    grey = ctk.CTkFrame(
        root,
        width=210,
        height=160,
        corner_radius=18,
        fg_color="#D9D9D9",
    )
    grey.place(x=965 + col*225, y=600 + row*180)
    grey_frames.append(grey)

Grey_1_label = ctk.CTkLabel(
    grey_frames[0],
    text=(
        "Людей осталось"
    ),
    font=("Arial", 18, "bold"),
    text_color="#000000",
)
Grey_1_label.place(x=40, y=7)
Grey_1_label2 = ctk.CTkLabel(
    grey_frames[0],
    text=(
        "  ____________"
    ),
    font=("Arial", 18, "bold"),
    text_color="#000000",
)
Grey_1_label2.place(x=40, y=80)



Grey_2_label = ctk.CTkLabel(
    grey_frames[1],
    text=(
        "Коробок осталось"
    ),
    font=("Arial", 18, "bold"),
    text_color="#000000",
)
Grey_2_label2 = ctk.CTkLabel(
    grey_frames[1],
    text=(
        "  ____________"
    ),
    font=("Arial", 18, "bold"),
    text_color="#000000",
)
Grey_2_label2.place(x=40, y=80)


Grey_2_label.place(x=35, y=7)

Grey_3_label = ctk.CTkLabel(
    grey_frames[2],
    text=(
        "Людей осталось"
    ),
    font=("Arial", 18, "bold"),
    text_color="#000000",
)
Grey_3_label.place(x=35, y=7)

Grey_3_label2 = ctk.CTkLabel(
    grey_frames[2],
    text=(
        "  ____________"
    ),
    font=("Arial", 18, "bold"),
    text_color="#000000",
)
Grey_3_label2.place(x=40, y=80)

Grey_4_label = ctk.CTkLabel(
    grey_frames[3],
    text=(
        "Количество попыток "
    ),
    font=("Arial", 18, "bold"),
    text_color="#000000",
)
Grey_4_label.place(x=12, y=7)

Grey_4_label2 = ctk.CTkLabel(
    grey_frames[3],
    text=(
        "успешные__________"
    ),
    font=("Arial", 18, "bold"),
    text_color="#000000",
)
Grey_4_label2.place(x=5, y=50)

Grey_4_label3 = ctk.CTkLabel(
    grey_frames[3],
    text=(
        "провалы  __________"
    ),
    font=("Arial", 18, "bold"),
    text_color="#000000",
)
Grey_4_label3.place(x=5, y=85)


root.mainloop()