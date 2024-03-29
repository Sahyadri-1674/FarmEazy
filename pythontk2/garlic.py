from tkinter import *
from PIL import Image,ImageTk

class garlic_info:
    def __init__(self,root):
      self.root=root
      self.root.title("GARLIC")
      self.root.geometry("1000x650+0+0")
      self.root.config(bg = "orange")

      img1=Image.open(r"pythontk2/image/garlicin.jpg")
      img1=img1.resize((380,400),Image.ANTIALIAS)
      self.photoimg1=ImageTk.PhotoImage(img1)

      lbl=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE,bg="green")
      lbl.place(x=300,y=100,width=500,height=450)

      img2=Image.open(r"pythontk2/image/garlic.jpg")
      img2=img2.resize((250,200),Image.ANTIALIAS)
      self.photoimg2=ImageTk.PhotoImage(img2)

      lbl=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
      lbl.place(x=25,y=125,width=250,height=200)


if __name__=="__main__":
    root = Tk()
    obj=garlic_info(root)
    root.mainloop()

    
