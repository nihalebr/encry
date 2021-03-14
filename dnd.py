import tkinter
from tkinter.messagebox import showinfo
import windnd

def dragged_files(files):
    fn=files[0]
    print(type(fn))
    msg='\n'.join((item.decode('gbk') for item in files))
    showinfo("file",msg)

tk=tkinter.Tk()
windnd.hook_dropfiles(tk,func=dragged_files)
tk.mainloop()