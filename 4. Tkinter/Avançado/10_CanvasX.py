import tkinter as tk

class DrawApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Desenho Interativo")
        
        self.canvas = tk.Canvas(root, width=400, height=300, bg='white')
        self.canvas.pack()

        # Inicializa variáveis para armazenar coordenadas
        self.start_x = None
        self.start_y = None
        self.line = None

        # Configura eventos de mouse
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

    def start_draw(self, event):
        # Captura coordenadas iniciais do mouse
        self.start_x = event.x
        self.start_y = event.y

    def draw(self, event):
        # Desenha uma linha enquanto o botão do mouse estiver pressionado
        if self.start_x and self.start_y:
            if self.line:
                self.canvas.delete(self.line)
            self.line = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill='black')

    def stop_draw(self, event):
        # Limpa as coordenadas ao soltar o botão do mouse
        self.start_x = None
        self.start_y = None

def main():
    root = tk.Tk()
    app = DrawApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
