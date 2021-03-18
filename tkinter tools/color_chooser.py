from tkinter import *

from tkinter import colorchooser

HEIGHT = 200
WIDTH = 200
TITLE = "COLOR CHOOSER"
BACKGROUND = "darkgray"
FONT = "san_serif"

class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack(fill = BOTH, expand = 1)
        self.create_widgets()


    def create_widgets(self):
        menubar = Menu(self.master)
        self.master.config(menu = menubar)
        fileMenu = Men(menubar)
        fileMenu.add_command(label="open", command = self.onOpen)
        menubar.add_cascade(label = "File", menu = fileMenu)

        self.txt = Text(self)
        self.txt.pack(fill=Both, expand = 1)



        self.btn = Button(self, text = "choose color",
                          command = self.onChoose)
        self.btn.place(x=30, y=30)

        self.frame = Frame(self, border = 1,
                           relief = SUNKEN, width = 100, height = 100)
        self.frame.place(x=160, y=30)
    def onChoose(self):
        (rgb, hx) = colorchooser.askcolor()
        self.frame.config(bg=hx)



def main():
    root = Tk()
    root.geometry("250x750")
    app = App(root)
    root.mainloop()

main()
