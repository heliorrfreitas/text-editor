from tkinter import *
from tkinter.filedialog import *

filename = None
def new_file():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def save_file():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def save_file_as():
    f = asksaveasfile(mode='w', defaultextension=".txt")
    t = text.get(0.0, END)
    
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Error", message="Unable to save file.")

    global filename
    filename = f.name

def open_file():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)
    global filename
    filename = f.name

root = Tk()
root.title("Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", accelerator="Ctrl+S", command=save_file)
filemenu.add_command(label="Save As...", command=save_file_as)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()


# Tutorial from https://www.youtube.com/watch?v=xqDonHEYPgA