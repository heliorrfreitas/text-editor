import tkinter as tk
from tkinter.filedialog import *
import sys

class App(tk.Tk):

    def quit(self, event):
        print("quitting...")
        sys.exit(0)

    def new(self, event): 
        print("new file ...")       
        self.filename = "Untitled"
        self.text.delete(0.0, tk.END)    
    
    def save(self, event):
        print('update file...')
        t = self.text.get(0.0, tk.END)
        f = open(self.filename, 'w')
        f.write(t)
        f.close()
    
    def saveas(self, event):
        print("Save file as...")
        f = tk.filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        t = self.text.get(0.0, tk.END)
        
        try:
            f.write(t.rstrip())
        except:
            self.showerror(title="Error", message="Unable to save file.")

        self.filename = f.name
    
    def open(self, event):
        print("Open file...")
        f = tk.filedialog.askopenfile(mode='r')
        t = f.read()
        self.text.delete(0.0, tk.END)
        self.text.insert(0.0, t)
        self.filename = f.name


    def menuoptions(self, event):
        print("AQUI")

    def __init__(self):
        tk.Tk.__init__(self)

        self.title("My First Text Editor")
        self.minsize(width=400, height=400)
        self.maxsize(width=400, height=400)
        
        menubar = tk.Menu(self)
        
        filemenu = tk.Menu(menubar, tearoff=False)
        
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        

        filemenu.add_command(label="New", underline=1,
                                command=quit, accelerator="Ctrl+N")

        filemenu.add_command(label="Open", underline=2,
                                command=open, accelerator="Ctrl+O")

        filemenu.add_command(label="Save", underline=3,
                                command=quit, accelerator="Ctrl+S")


        filemenu.add_command(label="Save As...", underline=4,
                                command=quit, accelerator="Ctrl+Shift+S")

        
        filemenu.add_command(label="Exit", underline=5,
                                command=quit, accelerator="Ctrl+Q")



        self.config(menu=menubar)
        self.bind_all("<Control-n>", self.new)
        self.bind_all("<Control-q>", self.quit)
        self.bind_all("<Control-s>", self.save)
        self.bind_all("<Control-Shift-S>", self.saveas)
        self.bind_all("<Control-o>", self.open)
        
        self.filename = None
        
        self.text = Text(self, width=400, height=400)
        self.text.pack()

    

    
if __name__ == "__main__":
    app = App()
    app.mainloop()

