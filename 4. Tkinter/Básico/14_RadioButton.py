import tkinter as tk

root = tk.Tk()
var = tk.StringVar()

radiobutton1 = tk.Radiobutton(root, text="Opção 1", variable=var, value="1")
radiobutton1.pack()

radiobutton2 = tk.Radiobutton(root, text="Opção 2", variable=var, value="2")
radiobutton2.pack()

root.mainloop()
