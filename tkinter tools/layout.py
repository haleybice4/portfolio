from tkinter import *
from PIL import Image, ImageTk
HEIGHT = 750
WIDTH = 250

class App(Frame):
    def __init__(self,master):
        self.index = 0
        super(App, self).__init__(master)
        self.pack(fill = BOTH, expand = 1)
        self.create_widgits()


    def create_widgits(self):
        self.config(bg = "darkgrey")
        Label(text = "My Favorite Images", width = 20).place(x = (WIDTH/2)-70, y= 5)
        img1 = Image.open("good_plaid.jpeg")
        img2 = Image.open("good_polkadots.png")
        img3 = Image.open("good_stripes.jpeg")

        good_plaid = ImageTk.PhotoImage(img1)
        good_polkadots = ImageTk.PhotoImage(img2)
        good_stripes = ImageTk.PhotoImage(img3)
        self.imglist = [good_plaid, good_polkadots, good_stripes]

        self.imglbl1 = Label(self, image = self.imglist[0])
        self.imglbl1.image = good_plaid
        self.imglbl1.place(x = 25, y = 75)

        self.imglbl2 = Label(self, image=self.imglist[1])
        self.imglbl2.image = good_polkadots
        self.imglbl2.place(x=25, y=290)

        self.imglbl3 = Label(self, image=self.imglist[2])
        self.imglbl3.image = good_stripes
        self.imglbl3.place(x=25, y=525)

        change = Button(text="!", command=self.changeimg)
        change.place(x=25, y=740)

    def changeimg(self):
        self.index += 1
        if self.index>len(self.imglist)-1:
            self.index = 0

        self.imglbl1.config(image=self.imglist[self.index])
        self.imglbl2.config(image=self.imglist[self.index])
        self.imglbl3.config(image=self.imglist[self.index])

def main():
    root = Tk()
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))
    app = App(root)
    root.mainloop()

main()
