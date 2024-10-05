import tkinter as tk

root = tk.Tk()
root.title("Exemplo com fill e expand")

label1 = tk.Label(root, text="Label 1", bg="red")
label1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

label2 = tk.Label(root, text="Label 2", bg="green")
label2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

label3 = tk.Label(root, text="Label 3", bg="blue")
label3.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

root.mainloop()
