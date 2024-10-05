import tkinter as tk

root = tk.Tk()
root.title("Exemplo de configure com Variáveis")

# Variáveis para guardar estado
bg_color = tk.StringVar(value="white")
text_color = tk.StringVar(value="black")

# Função para mudar as propriedades
def mudar_propriedades():
    label.configure(bg=bg_color.get(), fg=text_color.get())

# Criando o Label
label = tk.Label(root, text="Texto Inicial", bg="white", fg="black", font=("Arial", 12))
label.pack(pady=20)

# Criando botões para mudar as variáveis
button1 = tk.Button(root, text="Fundo Azul", command=lambda: bg_color.set("blue"))
button1.pack(pady=5)

button2 = tk.Button(root, text="Texto Vermelho", command=lambda: text_color.set("red"))
button2.pack(pady=5)

# Botão para aplicar mudanças
button_apply = tk.Button(root, text="Aplicar Mudanças", command=mudar_propriedades)
button_apply.pack(pady=20)

root.mainloop()
