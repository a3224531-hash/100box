import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")


class PrisonersApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("100 Prisoners Dilemma")
        self.geometry("1440x1024")
        self.resizable(False, False)
        self.configure(fg_color="#000000")

        # Кнопка Выход
        self.exit_btn = ctk.CTkButton(self, text="Выход", fg_color="#1a8a4d",
                                      hover_color="#146c3c", width=100, height=35,
                                      corner_radius=15, font=("Arial", 16, "bold"))
        self.exit_btn.place(x=30, y=30)

        # Основной контейнер - размеры заданы в конструкторе
        self.main_container = ctk.CTkFrame(self, fg_color="transparent", width=1300, height=900)
        self.main_container.place(relx=0.5, rely=0.5, anchor="center")

        self._build_top_section()
        self._build_middle_section()
        self._build_bottom_section()

    def _build_top_section(self):
        top_frame = ctk.CTkFrame(self.main_container, fg_color="transparent", height=350)
        top_frame.pack(fill="x", pady=(0, 20))
        top_frame.pack_propagate(False)

        # Логотип (Кубик)
        logo_bg = ctk.CTkFrame(top_frame, width=180, height=180, fg_color="#1db954", corner_radius=40)
        logo_bg.pack(side="left", padx=(0, 40))
        logo_bg.pack_propagate(False)

        try:
            dice_img = ctk.CTkImage(Image.open("dice.png"), size=(120, 120))
            ctk.CTkLabel(logo_bg, image=dice_img, text="").place(relx=0.5, rely=0.5, anchor="center")
        except:
            ctk.CTkLabel(logo_bg, text="🎲", font=("Arial", 100)).place(relx=0.5, rely=0.5, anchor="center")

        # Заголовки
        title_box = ctk.CTkFrame(top_frame, fg_color="transparent")
        title_box.pack(side="left", fill="y", pady=20)

        ctk.CTkLabel(title_box, text="МАТЕМАТИЧЕСКАЯ ГОЛОВОЛОМКА", font=("Arial", 22, "bold"), text_color="white").pack(
            anchor="w")
        ctk.CTkLabel(title_box, text="100 Заключенных", font=("Arial", 78, "bold"), text_color="white").pack(anchor="w",
                                                                                                             pady=(5,
                                                                                                                   10))
        ctk.CTkLabel(title_box, text="Классическая задача о вероятности и выживании • Стратегия циклов • 31% успеха",
                     font=("Arial", 18), text_color="#aaaaaa").pack(anchor="w")

        # Карточка правил
        rules_card = ctk.CTkFrame(top_frame, fg_color="#0d0d0d", corner_radius=25, border_width=1,
                                  border_color="#333333", width=460, height=330)
        rules_card.pack(side="right")
        rules_card.pack_propagate(False)

        ctk.CTkLabel(rules_card, text="Правила игры", font=("Arial", 24, "bold"), text_color="#1db954").pack(anchor="w",
                                                                                                             padx=30,
                                                                                                             pady=(25,
                                                                                                                   15))
        rules_text = (
            "• 100 заключённых и 100 коробок\n"
            "• В каждой коробке случайный номер\n"
            "• Можно открыть до 50 коробок\n"
            "• Цель: найти свой номер\n"
            "• Все выживают, только если КАЖДЫЙ найдёт\n"
            "• Заключённые не могут общаться"
        )
        ctk.CTkLabel(rules_card, text=rules_text, font=("Arial", 16), justify="left", text_color="#999999",
                     line_spacing=10).pack(padx=30, anchor="w")

    def _build_middle_section(self):
        # Фрейм настроек
        settings_bar = ctk.CTkFrame(self.main_container, fg_color="#0d0d0d", corner_radius=25, border_width=1,
                                    border_color="#222222", height=120)
        settings_bar.pack(fill="x", pady=(0, 30))
        settings_bar.pack_propagate(False)

        # Секция настроек внутри
        inner_s = ctk.CTkFrame(settings_bar, fg_color="transparent")
        inner_s.pack(fill="both", padx=40, pady=15)

        # Лево
        s_left = ctk.CTkFrame(inner_s, fg_color="transparent")
        s_left.pack(side="left")
        ctk.CTkLabel(s_left, text="⚙ Настройки симуляции", font=("Arial", 14, "bold"), text_color="#1db954").pack(
            anchor="w")
        ctk.CTkLabel(s_left, text="Количество заключенных", font=("Arial", 13), text_color="white").pack(side="left",
                                                                                                         padx=(0, 10))
        for v in ["10", "50", "100"]:
            color = "#1db954" if v == "100" else "#2b2b2b"
            ctk.CTkButton(s_left, text=v, width=65, height=32, fg_color=color, font=("Arial", 14, "bold")).pack(
                side="left", padx=3)

        # Право
        s_right = ctk.CTkFrame(inner_s, fg_color="transparent")
        s_right.pack(side="right")
        ctk.CTkLabel(s_right, text="Количество Игр в быстрой симуляции", font=("Arial", 13), text_color="white").pack(
            side="left", padx=(0, 10))
        for v in ["100", "500", "1000"]:
            ctk.CTkButton(s_right, text=v, width=65, height=32, fg_color="#2b2b2b", font=("Arial", 14, "bold")).pack(
                side="left", padx=3)

        # Блок стратегий
        strat_frame = ctk.CTkFrame(self.main_container, fg_color="#0d0d0d", corner_radius=30, border_width=1,
                                   border_color="#222222", height=200)
        strat_frame.pack(fill="x", pady=(0, 30))
        strat_frame.pack_propagate(False)

        ctk.CTkLabel(strat_frame, text="Выберите стратегию", font=("Arial", 32, "bold"), text_color="white").place(x=40,
                                                                                                                   y=25)

        # Кнопки стратегий (сделал более яркими)
        ctk.CTkButton(strat_frame, text="Стратегия Циклов", fg_color="#1db954", hover_color="#18a049",
                      height=90, width=450, font=("Arial", 34, "bold"), corner_radius=20).place(x=40, y=85)
        ctk.CTkButton(strat_frame, text="Случайная", fg_color="#3a3a3a", hover_color="#4a4a4a",
                      height=90, width=450, font=("Arial", 34, "bold"), corner_radius=20).place(x=520, y=85)

        # Блок ПУСК
        play_btn_bg = ctk.CTkFrame(strat_frame, fg_color="#1db954", width=130, height=130, corner_radius=35)
        play_btn_bg.place(x=1120, y=20)
        ctk.CTkLabel(play_btn_bg, text="▶", font=("Arial", 70), text_color="white").place(relx=0.5, rely=0.45,
                                                                                          anchor="center")
        ctk.CTkLabel(strat_frame, text="ПУСК", font=("Arial", 28, "bold"), text_color="#1db954").place(x=1140, y=155)

    def _build_bottom_section(self):
        bottom_row = ctk.CTkFrame(self.main_container, fg_color="transparent")
        bottom_row.pack(fill="both", expand=True)

        # Сетка (Левая панель)
        grid_panel = ctk.CTkFrame(bottom_row, fg_color="#0d0d0d", corner_radius=30, border_width=1,
                                  border_color="#222222")
        grid_panel.pack(side="left", fill="both", expand=True, padx=(0, 20))

        # Центрированная сетка 20x5
        grid_inner = ctk.CTkFrame(grid_panel, fg_color="transparent")
        grid_inner.place(relx=0.5, rely=0.5, anchor="center")

        for i in range(100):
            r, c = divmod(i, 20)
            ctk.CTkButton(grid_inner, text=str(i + 1), width=54, height=54, fg_color="#1db954",
                          hover_color="#18a049", font=("Arial", 18, "bold"), corner_radius=10).grid(row=r, column=c,
                                                                                                    padx=4, pady=4)

        # Статистика (Правая панель)
        stats_panel = ctk.CTkFrame(bottom_row, fg_color="transparent")
        stats_panel.pack(side="right", fill="y")

        stats = [("Всего игр", "#0"), ("Успех %", "#0"), ("Успешных", "#0"), ("Провалов", "#0")]

        for idx, (title, val) in enumerate(stats):
            r, c = divmod(idx, 2)
            card = ctk.CTkFrame(stats_panel, fg_color="#0d0d0d", border_width=2, border_color="#1db954",
                                corner_radius=20, width=130, height=130)
            card.grid(row=r, column=c, padx=10, pady=10)
            card.pack_propagate(False)
            ctk.CTkLabel(card, text=title, font=("Arial", 14, "bold"), text_color="#1db954").pack(pady=(30, 5))
            ctk.CTkLabel(card, text=val, font=("Arial", 26, "bold"), text_color="white").pack()


if __name__ == "__main__":
    app = PrisonersApp()
    app.mainloop()