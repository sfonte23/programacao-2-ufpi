import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Exemplo de Canvas - Bitmap")

    canvas = tk.Canvas(root, width=400, height=300, bg='white')
    canvas.pack()

    # Carrega uma imagem bitmap
    bm = tk.BitmapImage(file='example.xbm')
    canvas.create_bitmap(200, 150, bitmap=bm, foreground='red')

    root.mainloop()

if __name__ == "__main__":
    main()
