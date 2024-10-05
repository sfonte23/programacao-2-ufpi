import tkinter as tk

root = tk.Tk()
listbox = tk.Listbox(root)
listbox.pack()

listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")
listbox.insert(tk.END, "Item 3")

root.mainloop()
