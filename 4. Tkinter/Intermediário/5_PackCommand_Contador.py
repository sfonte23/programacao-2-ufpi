import tkinter as tk

# Função chamada quando o botão é clicado
def incrementar_contador():
    global contador
    contador += 1
    label_contador.config(text=str(contador))

# Inicializando o contador
contador = 0

# Criando a janela principal
root = tk.Tk()
root.title("Contador de Cliques")

# Frame principal para agrupar os widgets
frame = tk.Frame(root, bg="lightgray", padx=20, pady=20)
frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Label que mostra o valor do contador
label_contador = tk.Label(frame, text=str(contador), font=("Arial", 48), bg="lightgray")
label_contador.pack(pady=20)

# Botão para incrementar o contador
button_incrementar = tk.Button(frame, text="Clique em mim", font=("Arial", 14), command=incrementar_contador)
button_incrementar.pack(pady=20)

# Iniciando o loop principal da aplicação
root.mainloop()
