'''O método configure em Tkinter é uma ferramenta poderosa que permite alterar as propriedades de um widget após ele ter sido criado. Ele pode ser usado para modificar várias opções de configuração de um widget, como cor de fundo, cor do texto, fonte, etc.'''

import tkinter as tk

root = tk.Tk()
root.title("Exemplo de configure")

# Criando um Label
label = tk.Label(root, text="Texto Inicial", bg="white", fg="black", font=("Arial", 12))
label.pack(pady=20)

# Função para mudar as propriedades do Label
def mudar_propriedades():
    label.configure(text="Texto Modificado", bg="yellow", fg="blue", font=("Helvetica", 16, "italic"))

# Criando um Button que chama a função mudar_propriedades
button = tk.Button(root, text="Mudar Propriedades", command=mudar_propriedades)
button.pack(pady=20)

root.mainloop()
