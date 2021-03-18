from tkinter import *
class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()



        self.pep = BooleanVar()
        self.sau = BooleanVar()
        self.ham = BooleanVar()
        self.boolsvars= [self.pep, self.sau, self.ham,self.pep, self.sau, self.ham,self.pep, self.sau, self.ham,self.pep, self.sau, self.ham]
        self.toppings= ["pepperoni", "sausage", "ham","pepperoni", "sausage", "ham","pepperoni", "sausage", "ham","pepperoni", "sausage", "ham"]
        for r in range(4):
            for c in range(3):
                self.create_cb(self.toppings[c],self.boolsvars[c],r,c)

    def create_cb(self,words, ischecked, r, c):

        Checkbutton(self,
                    text = words,
                    variable = ischecked
                    ).grid(row = r, column= c)

    def order(self):
        print("order")






def main():
    root = Tk()
    root.title("check boxes")
    root.geometry("720x719")
    root.resizable(800, 800)
    app = App(root)
    root.mainloop()
main()