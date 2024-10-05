import tkinter as tk

def show_popup(event):
    menu_popup.post(event.x_root, event.y_root)

def hello():
    print("Olá!")

def quit_app():
    root.quit()

root = tk.Tk()
root.title("Exemplo de Menu Popup")

# Criando um Menu Popup
menu_popup = tk.Menu(root, tearoff=0)
menu_popup.add_command(label="Olá", command=hello)
menu_popup.add_command(label="Sair", command=quit_app)

# Associando o evento de clique do botão direito do mouse ao Menu Popup
root.bind("<Button-3>", show_popup)

root.mainloop()
