import tkinter as tk

root = tk.Tk()
var = tk.IntVar()

checkbutton = tk.Checkbutton(root, text="Aceito os termos", variable=var)
checkbutton.pack()

root.mainloop()
