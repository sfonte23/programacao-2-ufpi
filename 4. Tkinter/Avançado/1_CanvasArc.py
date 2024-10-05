import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Exemplo de Canvas - Arc")

    canvas = tk.Canvas(root, width=400, height=300, bg='white')
    canvas.pack()

    # Desenha um arco de círculo
    canvas.create_arc(50, 50, 150, 150, start=0, extent=180, fill='blue')

    root.mainloop()

if __name__ == "__main__":
    main()
