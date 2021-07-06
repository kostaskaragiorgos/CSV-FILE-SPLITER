from tkinter import Menu, Button, StringVar, OptionMenu, messagebox as msg, Tk, Label
from tkinter import simpledialog

def helpmenu():
    msg.showinfo("Help", "Split your csv files")

    
def aboutmenu():
    msg.showinfo("About", "CSV FILE SPLITER\nVersion 1.0")

class CsvFileSpliter():
    def __init__(self, master):
        self.master = master
        self.master.title("CSV FILE SPLITER")
        self.master.geometry("250x300")
        self.master.resizable(False, False)
        
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())


    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
def main():
    root = Tk()
    CsvFileSpliter(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()