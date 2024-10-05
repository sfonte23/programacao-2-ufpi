import tkinter as tk

# Criação da janela principal
root = tk.Tk()
root.title("Layout com Grid")
root.geometry("300x200")

# Criando Labels com grid
tk.Label(root, text="Linha 0, Coluna 0").grid(row=0, column=0)
tk.Label(root, text="Linha 0, Coluna 1").grid(row=0, column=1)
tk.Label(root, text="Linha 1, Coluna 0").grid(row=1, column=0)
tk.Label(root, text="Linha 1, Coluna 1").grid(row=1, column=1)

# Executa a janela
root.mainloop()
