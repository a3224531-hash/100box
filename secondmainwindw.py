from functools import partial
import tkinter as tk
from tkinter import messagebox
import random

class PrisonGame:
    def __init__(self, master):
        self.master = master
        self.master.title("проба 100 заключённых")
        self.master.configure(bg="#0a175d")

        self.boxes = list(range(1, 101))
        random.shuffle(self.boxes)

        self.prisoner_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 50

        self.buttons_frame = tk.Frame(master, bg="#0b1a6c")
        self.buttons_frame.grid(row=0, column=0, padx=40, pady=40)
        self.box_buttons = []

        for i in range(1, 101):
            btn = tk.Button(
                self.buttons_frame,
                text=str(i),
                width=8,
                height=3,
                bg="#e4a700",
                fg="black",
                font=("Arial", 10, "bold"),
                command=partial(self.open_box, i-1)
            )
            row = (i-1) // 10
            col = (i-1) % 10
            btn.grid(row=row, column=col, padx=2, pady=2)
            self.box_buttons.append(btn)  

        self.info_frame = tk.Frame(master, bg="#0a175d")
        self.info_frame.grid(row=0, column=1, sticky="n", padx=150)

        tk.Label(
            self.info_frame, 
            text=f"Твой номер: {self.prisoner_number}",
            fg="white", bg="#0a175d", font=("Arial", 17, "bold")
        ).pack(pady=10)

        self.attempts_label = tk.Label(
            self.info_frame, 
            text=f"Попытки: {self.attempts}/{self.max_attempts}",
            fg="white", bg="#0a175d", font=("Arial", 17, "bold")
        )
        self.attempts_label.pack(pady=10)

    def open_box(self, index):
        if self.attempts >= self.max_attempts:
            messagebox.showinfo("Результат", "лох")
            self.disable_all_buttons()
            return

        number_inside = self.new_method(index)

        self.box_buttons[index].config(text=str(number_inside), state="disabled")
        self.attempts_label.config(text=f"Попытки: {self.attempts}/{self.max_attempts}")

        if number_inside == self.prisoner_number:
            messagebox.showinfo("Результат", "Молодец! Ты нашёл свой номер!")
            self.disable_all_buttons()
        elif self.attempts == self.max_attempts:
            messagebox.showinfo("Результат", "не нашел")
            self.disable_all_buttons()

    def new_method(self, index):
        self.attempts += 1
        number_inside = self.boxes[index]
        return number_inside

    def disable_all_buttons(self):
        for btn in self.box_buttons:
            btn.config(state="disabled")

root = tk.Tk()
game = PrisonGame(root)
root.mainloop()