import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Exemplo de Canvas - Imagem")

    canvas = tk.Canvas(root, width=400, height=300, bg='white')
    canvas.pack()

    # Carrega uma imagem colorida
    img = tk.PhotoImage(file='image.gif')
    canvas.create_image(200, 150, image=img)

    root.mainloop()

if __name__ == "__main__":
    main()
