from tkinter import *

root = Tk()
root.title("Exemplo de Listbox com Scrollbar")

# Cria a Listbox
lbox = Listbox(root)
lbox.pack(side=LEFT, expand=True, fill="both")

# Cria a Scrollbar associada à Listbox
scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill="y")

# Configura a Scrollbar para controlar a Listbox
scroll.configure(command=lbox.yview)
lbox.configure(yscrollcommand=scroll.set)

# Adiciona itens à Listbox
for i in range(100):
    lbox.insert(END, i)

root.mainloop()
