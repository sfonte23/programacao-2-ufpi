import tkinter as tk

def mostrar_mensagem():
    label.config(text="Botão foi clicado!")

root = tk.Tk()
root.title("Exemplo Completo")

frame = tk.Frame(root, bg="lightgray", padx=10, pady=10)
frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

label = tk.Label(frame, text="Olá, Tkinter!", font=("Arial", 14), bg="lightgray")
label.pack(pady=10)

button = tk.Button(frame, text="Clique em mim", command=mostrar_mensagem)
button.pack(pady=10)

root.mainloop()
