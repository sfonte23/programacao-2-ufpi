import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Exemplo de Canvas - Linha")

    canvas = tk.Canvas(root, width=400, height=300, bg='white')
    canvas.pack()

    # Desenha uma linha poligonal
    canvas.create_line(50, 50, 150, 150, 250, 50, fill='green', width=3)

    root.mainloop()

if __name__ == "__main__":
    main()
