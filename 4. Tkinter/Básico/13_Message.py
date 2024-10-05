import tkinter as tk

root = tk.Tk()
message = tk.Message(root, text="Este é um widget Message.\nEle suporta várias linhas de texto.")
message.pack()

root.mainloop()
