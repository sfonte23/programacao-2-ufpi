import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Exemplo de Canvas - Retângulo")

    canvas = tk.Canvas(root, width=400, height=300, bg='white')
    canvas.pack()

    # Desenha um retângulo
    canvas.create_rectangle(100, 50, 300, 150, outline='green', fill='lightblue')

    root.mainloop()

if __name__ == "__main__":
    main()
