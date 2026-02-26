import tkinter as tk

app = tk.Tk()  #Создаём окно
app.title("пример")
app.geometry("400x200")
app.configure(bg="red")   #фон окна (можно менять)

label = tk.Label(

    root,
    text="Привет", 
    fg="yellow",          #fg — foreground (цвет текста)
    bg="red",            #bg — background (фиолетовый фон)
    font=("comforta", 20)     # шрифт и размер

)  

label.pack(pady=100)  

root.mainloop()