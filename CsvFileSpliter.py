""" Csv File Spliter"""
from tkinter import Menu, Button, messagebox as msg, Tk, Label
from tkinter import filedialog, Text, IntVar, Checkbutton
from tkinter.constants import END

import pandas as pd


def helpmenu():
    """help menu function"""
    msg.showinfo("Help", "Split your csv files")

    
def aboutmenu():
    """about menu function"""
    msg.showinfo("About", "CSV FILE SPLITER\nVersion 1.0")


def savefile():
    """the desired file name of the user.
    Returns:
        filenamesave: the name of the file
    """
    filenamesave = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                filetypes=(("csv files", "*.csv"),
                                                           ("all files", "*.*")))

    return filenamesave
class CsvFileSpliter():
    def __init__(self, master):
        self.master = master
        self.master.title("CSV FILE SPLITER")
        self.master.geometry("250x250")
        self.master.resizable(False, False)
        self.filename = ""
        self.df = ""
        self.subset = ""
        self.effectedlines = 0

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

        self.var2 = IntVar()
        self.chb2 = Checkbutton(master, text="Delete from orignial file", variable=self.var2)
        self.chb2.pack()

        self.splitb = Button(self.master, text="SPLIT", command=self.split)
        self.splitb.pack()
        
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Insert a csv file",
                                   accelerator='Ctrl+O', command=self.insertfile)
        self.file_menu.add_command(label="Close file", accelerator='Ctrl+F4',
                                   command=self.closefile)
        self.file_menu.add_command(label="Save file", accelerator="Ctrl+S",
                                   command=self.savesplitedfile)
        self.file_menu.add_command(label="Split", accelerator='Ctrl+F5',
                                   command=self.split)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)


        self.show_menu = Menu(self.menu, tearoff=0)
        self.show_menu.add_command(label="Show Splited", accelerator='Alt+F5',
                                   command=lambda: self.showinformation(str(self.subset),
                                                                        "SPLITED FILE"))
        self.show_menu.add_command(label="Show Effected Lines",
                                   accelerator="Alt+E",
                                   command=lambda: self.showinformation(str(self.effectedlines),
                                                                        "EFFECTED LINES"))
        self.menu.add_cascade(label="Show", menu=self.show_menu)
        
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('Control-o', lambda event: self.insertfile())
        self.master.bind('<Control-F4>', lambda evemt: self.closefile())
        self.master.bind('<Control-s>', lambda event: self.savesplitedfile())
        self.master.bind('<Control-F5>', lambda event: self.split())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Alt-F5>', lambda event: self.showinformation(str(self.subset),
                                                                        "SPLITED FILE"))
        self.master.bind('<Alt-e>', lambda event: self.showinformation(str(self.effectedlines),
                                                                       "EFFECTED LINES"))
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())

    def showinformation(self, typeofinfo=None, messagetitle=None):
        """
        Shows a type of information.
        Args:
            typeofinfo: the desired info
            messagetitle: the pop up window title
        """
        if not isinstance(self.subset, pd.DataFrame):
            msg.showerror("ERROR", "NO FILE TO SHOW")
        else:
            msg.showinfo(title=str(messagetitle), message=str(typeofinfo))

    def closefile(self):
        """ closes the csv file """
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV TO CLOSE")
        else:
            self.filename = ""
            self.df = ""
            msg.showinfo("SUSSESS", "YOUR CSV FILE HAS SUCCESFULLY CLOSED")

    def deletefromoriginal(self):
        """delete from the original file"""
        if self.var2.get():
            original = len(self.df)
            self.df.drop(self.df.index[int(self.startinglinet.get(1.0, END)) :int(self.lastlinet.get(1.0, END))], inplace=True)
            self.effectedlines += abs(original - len(self.df))

    
    def savesplitedfile(self):
        """saves the splited file"""
        self.subset = self.df.iloc[int(self.startinglinet.get(1.0, END)):int(self.lastlinet.get(1.0, END))]
        filenamesave = savefile()
        if ".csv" not in filenamesave:
            filenamesave = "test.csv"
        if self.var1.get():
            self.subset.to_csv(str(filenamesave), header=True)
        else:
            self.subset.to_csv(str(filenamesave), header=False)
        msg.showinfo("SUCCESS", "CSV FILE HAS SUCCESSFULLY SPLITED")



    def split(self):
        """the file split function"""
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE IMPORTED")
        elif int(str(self.startinglinet.get(1.0, END))) >= int(str(self.lastlinet.get(1.0, END))):
            msg.showerror("ERROR", "Starting line should be lower than the last line")
        elif  int(str(self.startinglinet.get(1.0, END))) < len(self.df) and int(str(self.lastlinet.get(1.0, END))) <= len(self.df):
            self.savesplitedfile()
            self.deletefromoriginal()
            

    def exitmenu(self):
        """exit menu function"""
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
    """main functionn"""
    root = Tk()
    CsvFileSpliter(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
