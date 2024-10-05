import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Exemplo de Canvas - Texto")

    canvas = tk.Canvas(root, width=400, height=300, bg='white')
    canvas.pack()

    # Exibe texto
    canvas.create_text(200, 150, text="Exemplo de Texto", font=("Arial", 20), fill='purple')

    root.mainloop()

if __name__ == "__main__":
    main()
