import tkinter as tk

root = tk.Tk()
root.title("Tipo e Cor da Letra")

# Label com tipo de letra e cor personalizados
label = tk.Label(root, text="Texto com fonte personalizada", font=("Helvetica", 16, "bold"), fg="red")
label.pack(pady=20)

root.mainloop()
