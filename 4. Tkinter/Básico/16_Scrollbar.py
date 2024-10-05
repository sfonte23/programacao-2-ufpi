import tkinter as tk

root = tk.Tk()
text = tk.Text(root, height=10, width=40)
scrollbar = tk.Scrollbar(root, command=text.yview)
text.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text.pack(side=tk.LEFT, fill=tk.BOTH)

root.mainloop()
