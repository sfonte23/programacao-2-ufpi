import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Exemplo de Canvas - Polígono")

    canvas = tk.Canvas(root, width=400, height=300, bg='white')
    canvas.pack()

    # Desenha um polígono
    canvas.create_polygon(50, 50, 150, 100, 200, 200, 100, 250, outline='red', fill='yellow')

    root.mainloop()

if __name__ == "__main__":
    main()
