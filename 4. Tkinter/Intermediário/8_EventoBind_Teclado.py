import tkinter as tk

def tecla_pressionada(event):
    label.config(text=f"Tecla pressionada: {event.keysym}")

def tecla_solta(event):
    label.config(text=f"Tecla solta: {event.keysym}")

# Criando a janela principal
root = tk.Tk()
root.title("Eventos de Teclado")

# Frame principal
frame = tk.Frame(root, width=300, height=200, bg="lightgray")
frame.pack(padx=10, pady=10)

# Label para exibir eventos
label = tk.Label(frame, text="Pressione qualquer tecla", font=("Arial", 12), bg="lightgray")
label.pack(pady=20)

# Bind de eventos de teclado
root.bind("<KeyPress>", tecla_pressionada)
root.bind("<KeyRelease>", tecla_solta)

root.mainloop()
