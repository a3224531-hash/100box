from logging import root
import tkinter as tk

app = tk()  #Создаём окно
root.title("пример")
root.geometry("400x200")
root.configure(bg="red")   #фон окна (можно менять)

label = tk.Label(
    root,
    text="Привет", 
    fg="yellow",          #fg — foreground (цвет текста)
    bg="red",            #bg — background (фиолетовый фон)
    font=("comforta", 20)     # шрифт и размер
)  

label.grid(row=0, column=0)  
root.mainloop()