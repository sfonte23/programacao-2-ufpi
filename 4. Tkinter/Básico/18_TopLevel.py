import tkinter as tk

root = tk.Tk()
top = tk.Toplevel()
top.title("Nova Janela")

label = tk.Label(top, text="Esta é uma nova janela Toplevel")
label.pack()

root.mainloop()
