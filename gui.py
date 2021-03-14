import tkinter as tk
from tkinter.messagebox import showinfo
import windnd

gui=tk.Tk()
gui.title('Encry v0.3')

mylable1=tk.Label(gui, text='The quick brown', font=("SourceSerifPro-Bold", 50))
mylable2=tk.Label(gui, text='my name is jhon')

mylable1.pack()
mylable2.pack()

textbox = tk.Text(height=0.2, width=10,borderwidth=0)
textbox.insert(tk.END, "Default")
textbox.pack(padx=20)

def default(event):
    current = textbox.get("1.0", tk.END)
    if current == "Default\n":
        textbox.delete("1.0", tk.END)
    elif current == "\n":
        textbox.insert("1.0", "Default")

textbox.bind("<FocusIn>", default)
textbox.bind("<FocusOut>", default)

def dragged_files(files):
    fn=files[0]
    textbox.insert(tk.END,fn)
    msg='\n'.join((item.decode('gbk') for item in files))
    showinfo("file",msg)
windnd.hook_dropfiles(gui,func=dragged_files)
gui.mainloop()