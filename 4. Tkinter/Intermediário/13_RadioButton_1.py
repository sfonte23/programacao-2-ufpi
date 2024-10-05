import tkinter as tk

aplicacao = tk.Tk()
aplicacao.title('Exemplo 13')

cor = tk.StringVar(aplicacao)
cor.set("black")

label = tk.Label(aplicacao, background=cor.get())
label.pack(fill='both', expand=True)

def colorir():
    label.configure(background=cor.get())

opcoes_cores = [
    ("Preto", "black"),
    ("Vermelho", "red"),
    ("Azul", "blue"),
    ("Verde", "green")
]

for texto, cor_valor in opcoes_cores:
    tk.Radiobutton(aplicacao, text=texto, value=cor_valor, variable=cor, command=colorir).pack(anchor='w')

aplicacao.mainloop()
