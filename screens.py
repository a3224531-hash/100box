import customtkinter as ctk
from PIL import Image, ImageDraw
import os
import simulator

BG_COLOR = "#000000"
FRAME_COLOR = "#1C1C1C"
GREEN_PRIMARY = "#0BA84A" # bright green like the screenshot
GREEN_SECONDARY = "#076A30" # darker green
TEXT_GREY = "#A8A8A8"
BTN_GREY = "#5E5E5E"

def get_rounded_dice(size, radius, bg_color):
    try:
        if os.path.exists("dice.png"):
            # Load original
            img = Image.open("dice.png").convert("RGBA")
            # Round the original dice image
            mask = Image.new("L", img.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.rounded_rectangle((0, 0, img.size[0], img.size[1]), radius=radius, fill=255)
            img.putalpha(mask)
            
            # Create a colored background box
            bg_img = Image.new("RGBA", (size, size), (0,0,0,0))
            draw = ImageDraw.Draw(bg_img)
            # Create rounded background
            # customtkinter handles alpha of background, but we can draw it
            # wait, if we create a PIL image with a background it might not match perfectly 
            # if we can just use ctk.CTkFrame it's better. But for CTkImage we might need it.
            return img
    except Exception:
        pass
    return None

class StartScreen(ctk.CTkFrame):
    def __init__(self, master, switch_to_auto_callback, switch_to_manual_callback):
        super().__init__(master, fg_color="transparent")
        self.switch_to_auto_callback = switch_to_auto_callback
        self.switch_to_manual_callback = switch_to_manual_callback
        
        # Center grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        center = ctk.CTkFrame(self, fg_color="transparent")
        center.grid(row=0, column=0)

        # DICE ICON with green background
        dice_frame = ctk.CTkFrame(center, width=180, height=180, fg_color=GREEN_PRIMARY, corner_radius=30)
        dice_frame.pack(pady=(0, 20))
        dice_frame.pack_propagate(False)
        dice_img = get_rounded_dice(180, 40, GREEN_PRIMARY)
        if dice_img:
            # Resize dice to fit in the box
            dice_img = dice_img.resize((130, 130), Image.Resampling.LANCZOS)
            ctk_dice = ctk.CTkImage(light_image=dice_img, dark_image=dice_img, size=(130, 130))
            ctk.CTkLabel(dice_frame, image=ctk_dice, text="").place(relx=0.5, rely=0.5, anchor="center")
        else:
            ctk.CTkLabel(dice_frame, text="🎲", font=("Arial", 100)).place(relx=0.5, rely=0.5, anchor="center")

        # TITLE
        ctk.CTkLabel(center, text="100", font=("Arial", 90, "bold"), text_color=GREEN_PRIMARY).pack(pady=(0, 0))
        ctk.CTkLabel(center, text="Заключенных", font=("Arial", 65, "bold"), text_color=GREEN_PRIMARY).pack(pady=(0, 5))
        
        # SUBTITLE
        ctk.CTkLabel(center, text="Классическая математическая головоломка", font=("Arial", 22, "bold"), text_color="#FFFFFF").pack(pady=(10, 10))

        # DESCRIPTION
        desc_text = ("Каждый заключенный должен найти свой номер в коробках. Используя\n"
                     "стратегию циклов, шанс выживания увеличивается с 0% до 31%")
        ctk.CTkLabel(center, text=desc_text, font=("Arial", 16), text_color=TEXT_GREY, justify="center").pack(pady=(0, 40))

        # START BUTTONS
        btn_frame = ctk.CTkFrame(center, fg_color="transparent")
        btn_frame.pack(pady=(0, 0))
        
        btn_manual = ctk.CTkButton(
            btn_frame, text="▶ Начать в ручную", font=("Arial", 28, "bold"), text_color="white",
            fg_color=GREEN_PRIMARY, hover_color=GREEN_SECONDARY,
            width=280, height=70, corner_radius=35,
            command=self.switch_to_manual_callback
        )
        btn_manual.pack(side="left", padx=10)
        
        btn_auto = ctk.CTkButton(
            btn_frame, text="▶ Начать в авто", font=("Arial", 28, "bold"), text_color="white",
            fg_color=GREEN_PRIMARY, hover_color=GREEN_SECONDARY,
            width=280, height=70, corner_radius=35,
            command=self.switch_to_auto_callback
        )
        btn_auto.pack(side="left", padx=10)

class GameScreen(ctk.CTkFrame):
    def __init__(self, master, switch_to_start_callback):
        super().__init__(master, fg_color="transparent")
        self.switch_to_start_callback = switch_to_start_callback
        self.simulator = simulator.PrisonersSimulator(num_prisoners=100)
        
        self.current_prisoners = 100
        self.current_games = 1000
        self.current_strategy = 'cycles' 
        
        # Root layout uses pack
        self.pack(fill="both", expand=True, padx=20, pady=20)
        
        # We will split screen into 3 specific vertical sections: Header, Strategy, Bottom(Grid+Stats)
        
        # --- 1. HEADER SECTION ---
        header_section = ctk.CTkFrame(self, fg_color="transparent")
        header_section.pack(fill="x", pady=(0, 10))
        
        # LEFT HALF of Header (Exit btn, Title, Settings)
        header_left = ctk.CTkFrame(header_section, fg_color="transparent")
        header_left.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        # Top-left EXIT button
        exit_btn = ctk.CTkButton(header_left, text="Выход", width=110, height=40, fg_color=GREEN_PRIMARY, 
                                 hover_color=GREEN_SECONDARY, font=("Arial", 18, "bold"), corner_radius=15, 
                                 command=self.switch_to_start_callback)
        exit_btn.pack(anchor="nw", pady=(0, 15))
        
        # Title row (Dice + Text)
        title_row = ctk.CTkFrame(header_left, fg_color="transparent")
        title_row.pack(fill="x", anchor="w")
        
        # Dice
        dice_frame = ctk.CTkFrame(title_row, width=180, height=180, fg_color=GREEN_PRIMARY, corner_radius=30)
        dice_frame.pack(side="left", padx=(10, 30))
        dice_frame.pack_propagate(False)
        dice_img = get_rounded_dice(180, 40, GREEN_PRIMARY)
        if dice_img:
            dice_img = dice_img.resize((140, 140), Image.Resampling.LANCZOS)
            ctk_dice = ctk.CTkImage(light_image=dice_img, dark_image=dice_img, size=(140, 140))
            ctk.CTkLabel(dice_frame, image=ctk_dice, text="").place(relx=0.5, rely=0.5, anchor="center")
        else:
            ctk.CTkLabel(dice_frame, text="🎲", font=("Arial", 90)).place(relx=0.5, rely=0.5, anchor="center")
            
        # Texts
        text_sub_frame = ctk.CTkFrame(title_row, fg_color="transparent")
        text_sub_frame.pack(side="left", anchor="center")
        ctk.CTkLabel(text_sub_frame, text="МАТЕМАТИЧЕСКАЯ ГОЛОВОЛОМКА", font=("Arial", 20, "bold"), text_color="#ffffff").pack(anchor="w")
        ctk.CTkLabel(text_sub_frame, text="100 Заключенных", font=("Arial", 56, "bold"), text_color="#ffffff").pack(anchor="w", pady=(0, 5))
        ctk.CTkLabel(text_sub_frame, text="Классическая задача о вероятности и выживании • Стратегия циклов • 31% успеха", font=("Arial", 16, "bold"), text_color="#ffffff").pack(anchor="w")

        # Settings block under Title row
        settings_bg = ctk.CTkFrame(header_left, fg_color=FRAME_COLOR, corner_radius=15, border_width=1, border_color="#333")
        settings_bg.pack(fill="x", pady=(15, 0), padx=(10, 0))
        settings_inner = ctk.CTkFrame(settings_bg, fg_color="transparent")
        settings_inner.pack(padx=20, pady=10, fill="x")

        ctk.CTkLabel(settings_inner, text="⚙ Настройки симуляции", font=("Arial", 18, "bold"), text_color=GREEN_PRIMARY).pack(anchor="w", pady=(0, 5))
        
        selectors_frame = ctk.CTkFrame(settings_inner, fg_color="transparent")
        selectors_frame.pack(fill="x")
        
        # Prisoners selector
        col1 = ctk.CTkFrame(selectors_frame, fg_color="transparent")
        col1.pack(side="left", expand=True, anchor="w")
        ctk.CTkLabel(col1, text="Количество заключенных", font=("Arial", 16, "bold"), text_color="white").pack(anchor="w")
        btn_row1 = ctk.CTkFrame(col1, fg_color="transparent")
        btn_row1.pack(pady=5, anchor="w")
        self.prisoner_btns = {}
        for val in [10, 50, 100]:
            btn = ctk.CTkButton(btn_row1, text=str(val), width=100, height=60, corner_radius=10,
                                fg_color=GREEN_PRIMARY if val == self.current_prisoners else BTN_GREY, 
                                font=("Arial", 22, "bold"), command=lambda v=val: self._set_prisoners(v))
            btn.pack(side="left", padx=(0, 10))
            self.prisoner_btns[val] = btn
            
        # Games selector
        col2 = ctk.CTkFrame(selectors_frame, fg_color="transparent")
        col2.pack(side="right", expand=True, anchor="e")
        ctk.CTkLabel(col2, text="Количество Игр в быстрой симуляции", font=("Arial", 16, "bold"), text_color="white").pack(anchor="w")
        btn_row2 = ctk.CTkFrame(col2, fg_color="transparent")
        btn_row2.pack(pady=5, anchor="w")
        self.games_btns = {}
        for val in [100, 500, 1000]:
            btn = ctk.CTkButton(btn_row2, text=str(val), width=100, height=60, corner_radius=10,
                                fg_color=BTN_GREY, 
                                font=("Arial", 22, "bold"), text_color="white", command=lambda v=val: self._set_games(v))
            if val == self.current_games:
                btn.configure(fg_color="#7A7A7A") 
            btn.pack(side="left", padx=(0, 10))
            self.games_btns[val] = btn


        # RIGHT HALF of Header (Rules)
        rules_frame = ctk.CTkFrame(header_section, fg_color=FRAME_COLOR, border_width=1, border_color="#333", corner_radius=15, width=600)
        rules_frame.pack(side="right", fill="y", padx=(20, 0))
        rules_frame.pack_propagate(False)

        ctk.CTkLabel(rules_frame, text="Правила игры", font=("Arial", 28, "bold"), text_color=GREEN_PRIMARY).pack(anchor="w", padx=25, pady=(25, 10))
        rules_text = (
            "• 100 заключенных и 100 коробок с номерами\n  от 1 до 100\n"
            "• В каждой коробке случайно размещен один\n  номер\n"
            "• Каждый заключенный может открыть\n  до 50 коробок\n"
            "• Цель: найти коробку со своим номером\n"
            "• Все выживают, только если КАЖДЫЙ найдет\n  свой номер\n"
            "• Заключенные не могут общаться после\n  начала игры"
        )
        ctk.CTkLabel(rules_frame, text=rules_text, font=("Arial", 20), justify="left", text_color=TEXT_GREY).pack(padx=25, pady=(0, 10), anchor="w")


        # --- 2. STRATEGY SELECTOR SECTION ---
        strat_container = ctk.CTkFrame(self, fg_color=FRAME_COLOR, corner_radius=15, border_width=1, border_color="#333")
        strat_container.pack(fill="x", pady=(5, 5))

        strat_inner = ctk.CTkFrame(strat_container, fg_color="transparent")
        strat_inner.pack(fill="x", padx=20, pady=15)

        strat_left = ctk.CTkFrame(strat_inner, fg_color="transparent")
        strat_left.pack(side="left", fill="x", expand=True)

        ctk.CTkLabel(strat_left, text="Выберите стратегию", font=("Arial", 36, "bold"), text_color="#ffffff").pack(anchor="w", pady=(0, 15))

        btn_box = ctk.CTkFrame(strat_left, fg_color="transparent")
        btn_box.pack(fill="x")

        self.btn_cycle = ctk.CTkButton(btn_box, text="Стратегия Циклов", fg_color=GREEN_PRIMARY, hover_color=GREEN_SECONDARY, height=100, font=("Arial", 42, "bold"), text_color="white", corner_radius=15, command=lambda: self._set_strategy('cycles'))
        self.btn_cycle.pack(side="left", expand=True, fill="x", padx=(0, 15))
        
        self.btn_random = ctk.CTkButton(btn_box, text="Случайная", fg_color=BTN_GREY, hover_color="#444", height=100, font=("Arial", 42, "bold"), text_color="white", corner_radius=15, command=lambda: self._set_strategy('random'))
        self.btn_random.pack(side="left", expand=True, fill="x", padx=(15, 0))

        # START Button (Play icon on top, ПУСК on bottom) -> Looks like a unified button in the screenshot
        start_btn = ctk.CTkButton(strat_inner, text="▶\nПУСК", fg_color=GREEN_PRIMARY, hover_color=GREEN_SECONDARY, text_color="white", font=("Arial", 42, "bold"), width=180, height=140, corner_radius=15, command=self._run_simulation)
        start_btn.pack(side="right", padx=(20, 0), anchor="s")


        # --- 3. BOTTOM SECTION (Grid + Stats) ---
        bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        bottom_frame.pack(fill="both", expand=True, pady=(5, 0))

        # Grid Block
        grid_bg = ctk.CTkFrame(bottom_frame, fg_color=FRAME_COLOR, corner_radius=15, border_width=1, border_color="#333")
        grid_bg.pack(side="left", fill="both", expand=True, padx=(0, 15))

        self.grid_container = ctk.CTkFrame(grid_bg, fg_color="transparent")
        self.grid_container.place(relx=0.5, rely=0.5, anchor="center")
        
        self._rebuild_grid()

        # Stats Block
        stats_pane = ctk.CTkFrame(bottom_frame, fg_color="transparent")
        stats_pane.pack(side="right", fill="y")

        stats_data = [
            ("Всего игр", "total_games", 0, 0), 
            ("Успех %", "success_percentage", 0, 1), 
            ("Успешных", "successes", 1, 0), 
            ("Провалов", "failures", 1, 1)
        ]
        self.stat_labels = {}

        for title, key, r, c in stats_data:
            # Stats boxes are dark inside with thin green borders
            card = ctk.CTkFrame(stats_pane, fg_color="#0F0F0F", border_color=GREEN_PRIMARY, border_width=2, corner_radius=15, height=155, width=165)
            card.grid(row=r, column=c, padx=8, pady=8)
            card.pack_propagate(False)
            
            inner = ctk.CTkFrame(card, fg_color="transparent")
            inner.place(relx=0.5, rely=0.5, anchor="center")
            
            ctk.CTkLabel(inner, text=title, font=("Arial", 18, "bold"), text_color=GREEN_PRIMARY).pack(pady=(0, 10))
            val_label = ctk.CTkLabel(inner, text="#0" if key != "success_percentage" else "#0%", font=("Arial", 38, "bold"), text_color="white")
            val_label.pack()
            self.stat_labels[key] = val_label

    def _rebuild_grid(self):
        for widget in self.grid_container.winfo_children():
            widget.destroy()
            
        # Per screenshot, 100 prisoners -> 20 columns, 5 rows
        columns = 20 if self.current_prisoners == 100 else 10 if self.current_prisoners == 50 else 5
        
        btn_width = 52 if self.current_prisoners == 100 else 80
        btn_height = 62 if self.current_prisoners == 100 else 80
        font_size = 32 if self.current_prisoners == 100 else 38

        for i in range(self.current_prisoners):
            r, c = divmod(i, columns)
            btn = ctk.CTkButton(self.grid_container, text=str(i + 1), width=btn_width, height=btn_height,
                                fg_color=GREEN_PRIMARY, hover_color=GREEN_SECONDARY, text_color="black",
                                font=("Arial", font_size, "bold"), corner_radius=8)
            btn.grid(row=r, column=c, padx=0, pady=2)

    def _set_prisoners(self, val):
        self.current_prisoners = val
        self.simulator = simulator.PrisonersSimulator(num_prisoners=val)
        for v, btn in self.prisoner_btns.items():
            btn.configure(fg_color=GREEN_PRIMARY if v == val else BTN_GREY)
        self._rebuild_grid()
        self._reset_stats()

    def _set_games(self, val):
        self.current_games = val
        for v, btn in self.games_btns.items():
            btn.configure(fg_color="#7A7A7A" if v == val else BTN_GREY)
            
    def _set_strategy(self, strat):
        self.current_strategy = strat
        self.btn_cycle.configure(fg_color=GREEN_PRIMARY if strat == 'cycles' else BTN_GREY)
        self.btn_random.configure(fg_color=GREEN_PRIMARY if strat == 'random' else BTN_GREY)

    def _reset_stats(self):
        self.stat_labels["total_games"].configure(text="#0")
        self.stat_labels["success_percentage"].configure(text="#0%")
        self.stat_labels["successes"].configure(text="#0")
        self.stat_labels["failures"].configure(text="#0")

    def _run_simulation(self):
        results = self.simulator.run_simulations(strategy=self.current_strategy, num_runs=self.current_games)
        
        self.stat_labels["total_games"].configure(text=f"#{results['total_games']}")
        self.stat_labels["success_percentage"].configure(text=f"#{results['success_percentage']}%")
        self.stat_labels["successes"].configure(text=f"#{results['successes']}")
        self.stat_labels["failures"].configure(text=f"#{results['failures']}")

class ManualGameScreen(ctk.CTkFrame):
    def __init__(self, master, switch_to_start_callback):
        super().__init__(master, fg_color="transparent")
        self.switch_to_start_callback = switch_to_start_callback
        
        import random
        self.boxes = list(range(1, 101))
        random.shuffle(self.boxes)
        
        self.current_prisoner = 0
        self.attempts_left = 50
        self.successful_prisoners = 0
        self.opened_boxes = set()
        
        self.pack(fill="both", expand=True, padx=40, pady=20)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)
        
        self._build_left_section()
        self._build_right_section()
        self._update_all_labels()
        
    def _build_left_section(self):
        left_frame = ctk.CTkFrame(self, fg_color="transparent", width=420)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=(50, 20), pady=(0, 0))
        left_frame.grid_propagate(False)
        
        exit_btn = ctk.CTkButton(left_frame, text="< Назад", width=80, height=35, fg_color="transparent", 
                                 hover_color="#333", font=("Arial", 18, "bold"), corner_radius=15, 
                                 command=self.switch_to_start_callback)
        exit_btn.pack(anchor="nw", pady=(10, 10))
        
        dice_frame = ctk.CTkFrame(left_frame, fg_color=GREEN_PRIMARY, corner_radius=50, width=360, height=360)
        dice_frame.pack(pady=(0, 10))
        dice_frame.pack_propagate(False)
        
        dice_img = get_rounded_dice(200, 50, GREEN_PRIMARY)
        if dice_img:
            dice_img = dice_img.resize((220, 220), Image.Resampling.LANCZOS)
            ctk_dice = ctk.CTkImage(light_image=dice_img, dark_image=dice_img, size=(220, 220))
            ctk.CTkLabel(dice_frame, image=ctk_dice, text="").place(relx=0.5, rely=0.5, anchor="center")
        else:
            ctk.CTkLabel(dice_frame, text="🎲", font=("Arial", 150)).place(relx=0.5, rely=0.5, anchor="center")
            
        ctk.CTkLabel(left_frame, text="100", font=("Arial", 80, "bold"), text_color="white").pack(pady=(0, 0))
        ctk.CTkLabel(left_frame, text="Заключенных", font=("Arial", 46, "bold"), text_color="white").pack(pady=(0, 40))
        
        self.prisoner_status_frame = ctk.CTkFrame(left_frame, fg_color=GREEN_PRIMARY, corner_radius=30, height=150, width=360)
        self.prisoner_status_frame.pack(pady=(0, 30))
        self.prisoner_status_frame.pack_propagate(False)
        
        self.lbl_prisoner = ctk.CTkLabel(self.prisoner_status_frame, text="Заключенный #0", font=("Arial", 22, "bold"), text_color="white")
        self.lbl_prisoner.place(x=25, y=30)
        
        self.lbl_attempts = ctk.CTkLabel(self.prisoner_status_frame, text="Попыток\nосталось:#0", font=("Arial", 22, "bold"), text_color="white", justify="left")
        self.lbl_attempts.place(x=25, y=70)
        
        bottom_stats_frame = ctk.CTkFrame(left_frame, fg_color="transparent", width=360)
        bottom_stats_frame.pack()
        
        self.box_success = ctk.CTkFrame(bottom_stats_frame, fg_color=GREEN_PRIMARY, corner_radius=25, height=140, width=175)
        self.box_success.pack(side="left", padx=(0, 5))
        self.box_success.pack_propagate(False)
        ctk.CTkLabel(self.box_success, text="Успешных\nзаключенных", font=("Arial", 14, "bold"), text_color="white", justify="left").place(x=15, y=20)
        self.lbl_successes = ctk.CTkLabel(self.box_success, text="#0/100", font=("Arial", 26, "bold"), text_color="white")
        self.lbl_successes.place(x=15, y=85)
        
        self.box_used = ctk.CTkFrame(bottom_stats_frame, fg_color=GREEN_PRIMARY, corner_radius=25, height=140, width=175)
        self.box_used.pack(side="left", padx=(5, 0))
        self.box_used.pack_propagate(False)
        ctk.CTkLabel(self.box_used, text="Использовано\nПопыток", font=("Arial", 14, "bold"), text_color="white", justify="left").place(x=15, y=20)
        self.lbl_used_attempts = ctk.CTkLabel(self.box_used, text="#0/50", font=("Arial", 26, "bold"), text_color="white")
        self.lbl_used_attempts.place(x=15, y=85)

    def _build_right_section(self):
        self.right_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.right_frame.grid(row=0, column=1, sticky="nsew")
        
        grid_wrapper = ctk.CTkFrame(self.right_frame, fg_color="transparent")
        grid_wrapper.place(relx=0.5, rely=0.5, anchor="center")
        
        self.grid_buttons = []
        for i in range(100):
            r, c = divmod(i, 10)
            btn = ctk.CTkButton(grid_wrapper, text=str(i + 1), width=85, height=85,
                                fg_color=GREEN_PRIMARY, hover_color=GREEN_SECONDARY, text_color="black",
                                font=("Arial", 44, "bold"), corner_radius=12,
                                command=lambda idx=i: self._on_box_click(idx))
            btn.grid(row=r, column=c, padx=3, pady=3)
            self.grid_buttons.append(btn)
            
    def _on_box_click(self, box_index):
        if self.current_prisoner >= 100 or self.attempts_left <= 0:
            return
            
        if box_index in self.opened_boxes:
            return
            
        self.opened_boxes.add(box_index)
        self.attempts_left -= 1
        
        slip_number = self.boxes[box_index]
        btn = self.grid_buttons[box_index]
        
        btn.configure(text=str(slip_number), text_color="white", fg_color=FRAME_COLOR, hover_color=FRAME_COLOR)
        
        self._update_all_labels()
        
        is_success = (slip_number == (self.current_prisoner + 1))
        
        if is_success:
            self.successful_prisoners += 1
            self._update_all_labels()
            self.after(800, self._next_prisoner)
        elif self.attempts_left == 0:
            self.after(800, self._failed_prisoner)
            
    def _failed_prisoner(self):
        self.current_prisoner = 100
        self._update_all_labels()
        
    def _next_prisoner(self):
        self.current_prisoner += 1
        if self.current_prisoner >= 100:
            self._update_all_labels()
            return
            
        self.attempts_left = 50
        self.opened_boxes.clear()
        
        for i, btn in enumerate(self.grid_buttons):
            btn.configure(text=str(i + 1), text_color="black", fg_color=GREEN_PRIMARY, hover_color=GREEN_SECONDARY)
            
        self._update_all_labels()
        
    def _update_all_labels(self):
        if self.current_prisoner >= 100:
            if self.successful_prisoners == 100:
                self.lbl_prisoner.configure(text="Победа!")
                self.lbl_attempts.configure(text="Все найдены!")
            else:
                self.lbl_prisoner.configure(text="Поражение!")
                self.lbl_attempts.configure(text="Не найден номер!")
        else:
            self.lbl_prisoner.configure(text=f"Заключенный #{self.current_prisoner}")
            self.lbl_attempts.configure(text=f"Попыток\nосталось:#{self.attempts_left}")
            
        self.lbl_successes.configure(text=f"#{self.successful_prisoners}/100")
        used_attempts = 50 - self.attempts_left if self.current_prisoner < 100 else 0
        self.lbl_used_attempts.configure(text=f"#{used_attempts}/50")
