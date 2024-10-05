import tkinter as tk

def clique_mouse(event):
    label.config(text=f"Mouse clicado na posição ({event.x}, {event.y})")

def movimento_mouse(event):
    label.config(text=f"Mouse movido para posição ({event.x}, {event.y})")

def tecla_pressionada(event):
    label.config(text=f"Tecla pressionada: {event.keysym}")

# Criando a janela principal
root = tk.Tk()
root.title("Exemplo de Eventos e Bind")

# Frame principal
frame = tk.Frame(root, width=300, height=200, bg="lightgray")
frame.pack(padx=10, pady=10)

# Label para exibir eventos
label = tk.Label(frame, text="Interaja com o mouse ou teclado", font=("Arial", 12), bg="lightgray")
label.pack(pady=20)

# Bind de eventos de mouse
frame.bind("<Button-1>", clique_mouse)
frame.bind("<Motion>", movimento_mouse)

# Bind de eventos de teclado
root.bind("<KeyPress>", tecla_pressionada)

root.mainloop()
