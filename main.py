import customtkinter as ctk
from screens import StartScreen, GameScreen

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1440x1024")
        self.title("100 Заключенных")
        self.configure(fg_color="#000000")
        
        ctk.set_appearance_mode("dark")
        
        self.current_screen = None
        self.show_start_screen()

    def show_start_screen(self):
        if self.current_screen:
            self.current_screen.destroy()
        
        self.current_screen = StartScreen(self, self.show_game_screen, self.show_manual_game_screen)
        self.current_screen.pack(fill="both", expand=True)

    def show_game_screen(self):
        if self.current_screen:
            self.current_screen.destroy()
            
        self.current_screen = GameScreen(self, self.show_start_screen)

    def show_manual_game_screen(self):
        if self.current_screen:
            self.current_screen.destroy()
            
        from screens import ManualGameScreen
        self.current_screen = ManualGameScreen(self, self.show_start_screen)
        # Note: the pack() is called inside GameScreen.__init__ because of the layout structure,
        # but to keep it consistent we can let GameScreen pack itself or do it here.
        # It's already packing itself in __init__.

if __name__ == "__main__":
    app = App()
    app.mainloop()