from tkinter import *

class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack(fill = BOTH, expand = 1)
        self.create_widgets()




    def create_widgets(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        fileMenu = Men(menubar)
        fileMenu.add_command(label="open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)

        self.txt = Text(self)
        self.txt.pack(fill=Both, expand=1)

    def onOpen(self):
        ftypes = [("python file", "*.py"),("Allfiles","*")]
        dlg = fileddialog.Open(self, filetype = ftypes)
        f1 = dlg.show()
        if f1 != "":
            text = self.readFile(f1)
            self.txt.insert(END, text)

    def readFile(self, filename):
        with open(filename, "r") as f:
            text = f.read()
            return text






    def main():
        root = Tk()
        root.geometry("250x750")
        app = App(root)
        root.mainloop()

main()