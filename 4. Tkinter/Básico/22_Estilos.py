import tkinter as tk

root = tk.Tk()
root.title("Personalização Completa")

# Alterando a cor de fundo da janela principal
root.configure(bg="lightgrey")

# Frame com fundo colorido
frame = tk.Frame(root, bg="lightblue", width=300, height=200)
frame.pack(padx=20, pady=20)

# Label dentro do Frame com estilo personalizado
label1 = tk.Label(frame, text="Texto no Frame", font=("Verdana", 12, "italic"), fg="darkgreen", bg="lightblue")
label1.pack(pady=10)

# Outra Label diretamente na janela principal
label2 = tk.Label(root, text="Texto na Janela Principal", font=("Courier", 16, "bold"), fg="purple", bg="lightgrey")
label2.pack(pady=20)

root.mainloop()
