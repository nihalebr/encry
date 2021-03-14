import tkinter as tk

"""tk.Tk()

textbox = tk.Text(height=10, width=10)
textbox.insert(tk.END, "Default")
textbox.pack()

# This is for demonstration purposes
tk.Text(height=10, width=10).pack()

def default(event):
    current = textbox.get("1.0", tk.END)
    if current == "Default\n":
        textbox.delete("1.0", tk.END)
    elif current == "\n":
        textbox.insert("1.0", "Default")

textbox.bind("<FocusIn>", default)
textbox.bind("<FocusOut>", default)"""
import tkinter as tk

class MyApp():
    def __init__(self):
        self.root = tk.Tk()
        l1 = tk.Label(self.root, text="Hello")
        l2 = tk.Label(self.root, text="World")
        l1.grid(row=0, column=0, padx=(100, 10))
        l2.grid(row=1, column=0, padx=(10, 100)) 

app = MyApp()
app.root.mainloop()
