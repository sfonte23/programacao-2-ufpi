import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Exemplo de Barras de Rolagem")

    # Cria um Canvas com barras de rolagem vertical e horizontal
    canvas = tk.Canvas(root, bg='white', width=300, height=200)
    canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Cria uma barra de rolagem vertical associada ao Canvas
    v_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=v_scrollbar.set)

    # Cria uma barra de rolagem horizontal associada ao Canvas
    h_scrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas.xview)
    h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
    canvas.configure(xscrollcommand=h_scrollbar.set)

    # Adiciona um grande retângulo ao Canvas para demonstrar a funcionalidade
    canvas.create_rectangle(0, 0, 1000, 800, fill='lightblue')

    root.mainloop()

if __name__ == "__main__":
    main()
