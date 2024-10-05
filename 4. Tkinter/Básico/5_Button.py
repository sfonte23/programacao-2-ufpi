import tkinter as tk

def on_button_click():
    print("Botão clicado!")

root = tk.Tk()
button = tk.Button(root, text="Clique em mim", command=on_button_click)
button.pack()
root.mainloop()
