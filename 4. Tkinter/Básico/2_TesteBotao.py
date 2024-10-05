import tkinter as tk

# Função que será chamada quando o botão for clicado
def on_button_click():
    label.config(text="Botão clicado!")

# Criação da janela principal
root = tk.Tk()
root.title("Exemplo com Widgets")
root.geometry("400x300")

# Criando um Label
label = tk.Label(root, text="Olá, Tkinter!")
label.pack(pady=10)

# Criando um Button
button = tk.Button(root, text="Clique em mim", command=on_button_click)
button.pack(pady=10)

# Criando um Entry
entry = tk.Entry(root)
entry.pack(pady=10)

# Executa a janela
root.mainloop()
