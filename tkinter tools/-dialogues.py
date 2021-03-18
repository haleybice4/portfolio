from tkinter import *
from tkinter import messagebox as mb


HEIGHT = 200
WIDTH = 200
TITLE = "new program"
BACKGROUND = "darkgray"
FONT = "san_serif"
class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack(fill = BOTH)
        self.create_widgits()


    def create_widgits(self):
       error = Button(self, text = "error", command = self.onError)
       error.grid(padx=5, pady=5)
       warning = Button(self, text = "warning", command = self.onWarn)
       warning.grid(row = 1, column = 0)
       question = Button(self, text = "question", command = self.onQuest)
       question.grid(row = 0, column = 1)
       inform = Button(self, text = "inform", command = self.onInfo)
       inform.grid(row = 1, column = 1)

    def onError(self):
        mb.showerror("Error","could nor open file")

    def onWarn(self):
        mb.showwarning("Warning", "deprecated function call")

    def onQuest(self):
        result = mb.askquestion("Question", "Are you sure to quit?")
        if result == "yes":
            print("you clicked yes")
        else:
            print("you clicked no")


    def onInfo(self):
        mb.showinfo("info", "download completed")




def main():
    root = Tk()
    root.geometry(str.format("{}x{}", WIDTH, HEIGHT))
    root.title(TITLE)
    root.config(bg = BACKGROUND)
    app = App(root)
    root.mainloop()

main()
