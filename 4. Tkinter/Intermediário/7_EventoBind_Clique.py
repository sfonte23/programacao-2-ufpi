import tkinter as tk

def clique_botao_esquerdo(event):
    label.config(text=f"Clique com o botão esquerdo na posição ({event.x}, {event.y})")

def clique_botao_direito(event):
    label.config(text=f"Clique com o botão direito na posição ({event.x}, {event.y})")

def duplo_clique(event):
    label.config(text=f"Duplo clique na posição ({event.x}, {event.y})")

def movimento_mouse(event):
    label.config(text=f"Mouse movido para posição ({event.x}, {event.y})")

# Criando a janela principal
root = tk.Tk()
root.title("Eventos de Clique do Mouse")

# Frame principal
frame = tk.Frame(root, width=300, height=200, bg="lightgray")
frame.pack(padx=10, pady=10)

# Label para exibir eventos
label = tk.Label(frame, text="Interaja com o mouse", font=("Arial", 12), bg="lightgray")
label.pack(pady=20)

# Bind de eventos de clique do mouse
frame.bind("<Button-1>", clique_botao_esquerdo)
frame.bind("<Button-3>", clique_botao_direito)
frame.bind("<Double-Button-1>", duplo_clique)
frame.bind("<Motion>", movimento_mouse)

root.mainloop()
