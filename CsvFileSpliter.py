from tkinter import Menu, Button, StringVar, OptionMenu, Widget, messagebox as msg, Tk, Label
from tkinter import simpledialog, filedialog, Text, IntVar, Checkbutton
from tkinter.constants import END

import pandas as pd

def helpmenu():
    msg.showinfo("Help", "Split your csv files")

    
def aboutmenu():
    msg.showinfo("About", "CSV FILE SPLITER\nVersion 1.0")

class CsvFileSpliter():
    def __init__(self, master):
        self.master = master
        self.master.title("CSV FILE SPLITER")
        self.master.geometry("250x250")
        self.master.resizable(False, False)
        self.filename = ""
        self.df = ""

        self.flineleb = Label(self.master, text="Enter the Starting Line")
        self.flineleb.pack()

        self.startinglinet = Text(self.master, height=1, width=4)
        self.startinglinet.pack()


        self.lastlineleb = Label(self.master, text="Enter the last Line")
        self.lastlineleb.pack()

        self.lastlinet = Text(self.master, height=1, width=4)
        self.lastlinet.pack()

        self.var1 = IntVar()
        self.chb = Checkbutton(master, text="Keep Columns", variable=self.var1)
        self.chb.pack()

        self.splitb = Button(self.master, text="SPLIT", command=self.split)
        self.splitb.pack()
        
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Insert a csv file",
                                   accelerator='Ctrl+O', command=self.insertfile)
        self.file_menu.add_command(label="Close file", accelerator='Ctrl+F4', command=self.closefile)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('Control-o', lambda event: self.insertfile())
        self.master.bind('<Control-F4>', lambda evemt: self.closefile())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())

    
    def closefile(self):
        """ closes the csv file """
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV TO CLOSE")
        else:
            self.filename = ""
            self.df = ""
            msg.showinfo("SUSSESS", "YOUR CSV FILE HAS SUCCESFULLY CLOSED")

    
    def savesplitedfile(self):
        subset = self.df.iloc[int(self.startinglinet.get(1.0,END)):int(self.lastlinet.get(1.0,END))]
        if self.var1 == 1:
            subset.to_csv("test.csv", header=True)
        else:
            subset.to_csv("test.csv", header=False)
        msg.showinfo("SUCCESS", "SUCCESS")

    def split(self):
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE IMPORTED")
        elif int(self.startinglinet.get(1.0,END)) >= int(self.lastlinet.get(1.0,END)):
                msg.showerror("ERROR", "Starting line should be lower than the last line")
        elif  int(self.startinglinet.get(1.0,END)) < len(self.df) and int(self.lastlinet.get(1.0,END)) <= len(self.df):
            self.savesplitedfile()

    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()

    def checkfile(self):
        """ checks if inserted file is a csv """
        if self.filename.endswith('.csv'):
            msg.showinfo("SUCCESSFUL INSERTION", "YOUR CSV FILE HAS SUCCESFULLY INSERTED")
            self.df = pd.read_csv(self.filename)
        else:
            msg.showerror("INSERT A CSV", "YOU HAVE TO INSERT A CSV FILE")
    

    def insertfile(self):
        """ inserts the csv file """
        if ".csv" in self.filename:
            msg.showerror("ERROR", "A CSV FILE IS ALREADY OPEN")
        else:
            self.filename = filedialog.askopenfilename(initialdir="/", title="Select csv file",
                                                        filetypes=(("csv files", "*.csv"),
                                                                    ("all files", "*.*")))
            self.checkfile()
def main():
    root = Tk()
    CsvFileSpliter(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()