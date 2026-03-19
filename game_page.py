import customtkinter as ctk
from PIL import Image
import tkinter as tk

ctk.set_appearance_mode("dark")


class PrisonersApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("100 Prisoners Dilemma Simulation")
        self.geometry("1100x800")
        self.configure(fg_color="#000000")  # Глубокий черный фон

        # Основной контейнер с отступами
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=30, pady=20)

        self._build_header()
        self._build_settings()
        self._build_strategy_selector()
        self._build_grid_and_stats()

    def _build_header(self):
        # Верхняя часть: Лого, Заголовок и Правила
        header_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        header_frame.pack(fill="x", pady=(0, 20))

        # Лево: Иконка и Текст
        title_section = ctk.CTkFrame(header_frame, fg_color="transparent")
        title_section.pack(side="left", anchor="n")

        # Имитация иконки кубика (зеленый квадрат с закруглением)
        dice_placeholder = ctk.CTkFrame(title_section, width=120, height=120, fg_color="#28a745", corner_radius=20)
        dice_placeholder.pack(side="left", padx=(0, 20))
        ctk.CTkLabel(dice_placeholder, text="🎲", font=("Arial", 60)).place(relx=0.5, rely=0.5, anchor="center")

        text_sub_frame = ctk.CTkFrame(title_section, fg_color="transparent")
        text_sub_frame.pack(side="left", anchor="c")

        ctk.CTkLabel(text_sub_frame, text="МАТЕМАТИЧЕСКАЯ ГОЛОВОЛОМКА", font=("Arial", 16, "bold"),
                     text_color="#ffffff").pack(anchor="w")
        ctk.CTkLabel(text_sub_frame, text="100 Заключенных", font=("Arial", 48, "bold"), text_color="#ffffff").pack(
            anchor="w")
        ctk.CTkLabel(text_sub_frame, text="Классическая задача о вероятности • Стратегия циклов • 31% успеха",
                     font=("Arial", 14), text_color="#28a745").pack(anchor="w")

        # Право: Правила игры
        rules_frame = ctk.CTkFrame(header_frame, fg_color="#121212", border_width=1, border_color="#333333",
                                   corner_radius=15, width=350)
        rules_frame.pack(side="right", fill="y", padx=(20, 0))

        ctk.CTkLabel(rules_frame, text="Правила игры", font=("Arial", 18, "bold"), text_color="#28a745").pack(
            anchor="w", padx=15, pady=(10, 5))
        rules_text = (
            "• 100 заключенных и 100 коробок\n"
            "• В каждой коробке случайный номер\n"
            "• Каждый может открыть до 50 коробок\n"
            "• Цель: найти свой номер\n"
            "• Выживут, если КАЖДЫЙ найдет свой\n"
            "• Общение запрещено"
        )
        ctk.CTkLabel(rules_frame, text=rules_text, font=("Arial", 13), justify="left", text_color="#cccccc").pack(
            padx=15, pady=(0, 10))

    def _build_settings(self):
        # Блок настроек
        settings_bg = ctk.CTkFrame(self.main_container, fg_color="#121212", corner_radius=15, height=100)
        settings_bg.pack(fill="x", pady=10)

        inner = ctk.CTkFrame(settings_bg, fg_color="transparent")
        inner.pack(pady=10, padx=20, fill="x")

        # Секция выбора количества
        col1 = ctk.CTkFrame(inner, fg_color="transparent")
        col1.pack(side="left")
        ctk.CTkLabel(col1, text="Количество заключенных", font=("Arial", 12, "bold"), text_color="#28a745").pack(
            anchor="w")

        btn_row1 = ctk.CTkFrame(col1, fg_color="transparent")
        btn_row1.pack(pady=5)
        for val in ["10", "50", "100"]:
            color = "#28a745" if val == "100" else "#333333"
            ctk.CTkButton(btn_row1, text=val, width=60, height=30, fg_color=color, font=("Arial", 12, "bold")).pack(
                side="left", padx=2)

        # Секция количества игр
        col2 = ctk.CTkFrame(inner, fg_color="transparent")
        col2.pack(side="right")
        ctk.CTkLabel(col2, text="Количество Игр в симуляции", font=("Arial", 12, "bold"), text_color="#28a745").pack(
            anchor="w")

        btn_row2 = ctk.CTkFrame(col2, fg_color="transparent")
        btn_row2.pack(pady=5)
        for val in ["100", "500", "1000"]:
            color = "#333333"
            ctk.CTkButton(btn_row2, text=val, width=60, height=30, fg_color=color).pack(side="left", padx=2)

    def _build_strategy_selector(self):
        # Выбор стратегии и ПУСК
        strat_container = ctk.CTkFrame(self.main_container, fg_color="transparent")
        strat_container.pack(fill="x", pady=20)

        left_part = ctk.CTkFrame(strat_container, fg_color="transparent")
        left_part.pack(side="left", fill="x", expand=True)

        ctk.CTkLabel(left_part, text="Выберите стратегию", font=("Arial", 24, "bold"), text_color="#ffffff").pack(
            anchor="w")

        btn_box = ctk.CTkFrame(left_part, fg_color="#1c1c1c", corner_radius=15, pady=15, padx=15)
        btn_box.pack(fill="x", pady=10)

        ctk.CTkButton(btn_box, text="Стратегия Циклов", fg_color="#28a745", height=60, font=("Arial", 20, "bold"),
                      text_color="white").pack(side="left", expand=True, fill="x", padx=5)
        ctk.CTkButton(btn_box, text="Случайная", fg_color="#333333", height=60, font=("Arial", 20, "bold"),
                      text_color="white").pack(side="left", expand=True, fill="x", padx=5)

        # Кнопка ПУСК
        start_btn = ctk.CTkButton(strat_container, text="▶\nПУСК", fg_color="transparent", text_color="#28a745",
                                  font=("Arial", 22, "bold"), width=100)
        start_btn.pack(side="right", padx=(20, 0))

    def _build_grid_and_stats(self):
        # Нижняя панель: Сетка 20x5 и Статистика
        bottom_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        bottom_frame.pack(fill="both", expand=True)

        # Сетка коробок
        grid_bg = ctk.CTkFrame(bottom_frame, fg_color="#121212", corner_radius=20, border_width=1,
                               border_color="#333333")
        grid_bg.pack(side="left", fill="both", expand=True, padx=(0, 20), pady=5)

        grid_container = ctk.CTkFrame(grid_bg, fg_color="transparent")
        grid_container.place(relx=0.5, rely=0.5, anchor="center")

        for i in range(100):
            r, c = divmod(i, 20)
            btn = ctk.CTkButton(grid_container, text=str(i + 1), width=42, height=42,
                                fg_color="#28a745", hover_color="#218838",
                                font=("Arial", 12, "bold"), corner_radius=6)
            btn.grid(row=r, column=c, padx=3, pady=3)

        # Статистика (4 плашки)
        stats_pane = ctk.CTkFrame(bottom_frame, fg_color="transparent", width=120)
        stats_pane.pack(side="right", fill="y")

        stats_data = [("Всего игр", "#0"), ("Успех %", "#0"), ("Успешных", "#0"), ("Провалов", "#0")]

        for title, value in stats_data:
            card = ctk.CTkFrame(stats_pane, fg_color="#121212", border_width=1, border_color="#28a745",
                                corner_radius=12, height=80, width=110)
            card.pack(pady=5)
            card.pack_propagate(False)
            ctk.CTkLabel(card, text=title, font=("Arial", 11, "bold"), text_color="#28a745").pack(pady=(10, 0))
            ctk.CTkLabel(card, text=value, font=("Arial", 18, "bold"), text_color="white").pack()


if __name__ == "__main__":
    app = PrisonersApp()
    app.mainloop()