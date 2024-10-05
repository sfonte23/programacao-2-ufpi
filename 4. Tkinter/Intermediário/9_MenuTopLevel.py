import tkinter as tk

def hello():
    print("Olá!")

def quit_app():
    root.quit()

root = tk.Tk()
root.title("Exemplo de Menu Toplevel")

# Criando um Menu Toplevel
menu_toplevel = tk.Menu(root)

# Adicionando opções ao Menu
menu_toplevel.add_command(label="Olá", command=hello)
menu_toplevel.add_separator()
menu_toplevel.add_command(label="Sair", command=quit_app)

# Associando o Menu Toplevel à janela principal
root.config(menu=menu_toplevel)

root.mainloop()
