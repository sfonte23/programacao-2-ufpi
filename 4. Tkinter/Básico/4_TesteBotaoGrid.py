import tkinter as tk

# Função para tratar o evento de clique do botão
def on_button_click(event):
    print(f"Botão clicado na posição ({event.x}, {event.y})")

# Criação da janela principal
root = tk.Tk()
root.title("Eventos em Tkinter")
root.geometry("300x200")

# Criando um Button e associando o evento de clique
button = tk.Button(root, text="Clique em mim")
button.bind("<Button-1>", on_button_click)
button.pack(pady=10)

# Executa a janela
root.mainloop()
