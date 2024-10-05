import tkinter as tk

root = tk.Tk()
root.title("Cor de Fundo")

# Label com fundo colorido
label = tk.Label(root, text="Texto com fundo azul", bg="blue", fg="white")
label.pack(pady=20)

root.mainloop()
