import tkinter as tk

def on_button_click():
    print("Botão clicado!")

root = tk.Tk()
root.title("Exemplo de Command")

button = tk.Button(root, text="Clique em mim", command=on_button_click)
button.pack(pady=20)

root.mainloop()
