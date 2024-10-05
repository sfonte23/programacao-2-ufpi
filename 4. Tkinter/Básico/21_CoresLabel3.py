import tkinter as tk

root = tk.Tk()
root.title("Parte da Janela Colorida")

# Frame com fundo colorido
frame = tk.Frame(root, bg="lightgreen", width=300, height=200)
frame.pack(padx=10, pady=10)

# Label dentro do Frame com estilo personalizado
label = tk.Label(frame, text="Texto dentro do Frame", font=("Arial", 14), fg="blue", bg="lightgreen")
label.pack(pady=20)

root.mainloop()
