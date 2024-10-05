import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Exemplo de Canvas - Oval")

    canvas = tk.Canvas(root, width=400, height=300, bg='white')
    canvas.pack()

    # Desenha um círculo (oval)
    canvas.create_oval(100, 50, 300, 150, outline='blue', width=2)

    root.mainloop()

if __name__ == "__main__":
    main()
