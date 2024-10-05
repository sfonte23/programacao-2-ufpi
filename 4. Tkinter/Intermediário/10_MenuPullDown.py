import tkinter as tk

def hello():
    print("Olá!")

def Open():
    print("Abrindo!")

def quit_app():
    root.quit()

root = tk.Tk()
root.title("Exemplo de Menu Pulldown")

# Criando um Menu Toplevel
menu_toplevel = tk.Menu(root)

# Criando um Menu Pulldown
menu_arquivo = tk.Menu(menu_toplevel, tearoff=0)
menu_toplevel.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Novo", command=hello)
menu_arquivo.add_command(label="Abrir", command=Open)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=quit_app)

# Associando o Menu Toplevel à janela principal
root.config(menu=menu_toplevel)

root.mainloop()
