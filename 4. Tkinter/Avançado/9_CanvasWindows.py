import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Exemplo de Canvas - Componente Tk")

    canvas = tk.Canvas(root, width=400, height=300, bg='white')
    canvas.pack()

    # Exibe um botão dentro do Canvas
    button = tk.Button(canvas, text="Clique-me")
    canvas.create_window(200, 150, window=button)

    root.mainloop()

if __name__ == "__main__":
    main()
