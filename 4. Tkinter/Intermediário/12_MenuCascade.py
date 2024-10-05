import tkinter as tk

def hello():
    print("Olá!")

def quit_app():
    root.quit()

root = tk.Tk()
root.title("Exemplo de Menu em Cascata")

# Criando um Menu Toplevel
menu_toplevel = tk.Menu(root)

# Criando um Menu Cascata
menu_arquivo = tk.Menu(menu_toplevel, tearoff=0)
menu_editar = tk.Menu(menu_toplevel, tearoff=0)

menu_toplevel.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Novo", command=hello)
menu_arquivo.add_command(label="Abrir", command=hello)
menu_arquivo.add_separator()
menu_arquivo.add_cascade(label="Editar", menu=menu_editar)
menu_editar.add_command(label="Cortar", command=hello)
menu_editar.add_command(label="Copiar", command=hello)
menu_editar.add_command(label="Colar", command=hello)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=quit_app)

# Associando o Menu Toplevel à janela principal
root.config(menu=menu_toplevel)

root.mainloop()
