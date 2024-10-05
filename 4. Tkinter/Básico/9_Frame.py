import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, text="Dentro do Frame")
label.pack()

root.mainloop()
