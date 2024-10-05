import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Desenhando uma linha
canvas.create_line(0, 0, 400, 300, fill="blue")

# Desenhando um retângulo
canvas.create_rectangle(50, 50, 150, 150, fill="red")

root.mainloop()
