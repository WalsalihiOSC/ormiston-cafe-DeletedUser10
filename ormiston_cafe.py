"""Modules used"""
from logging import root
from tkinter import*
import json
from PIL import ImageTk,Image

"""Clas for first window's interface""" 
class First_window:
    def __init__(self, parent):
        self.imgs = Temp_img()
        """Loads json database"""
        with open("Data.json", "r") as file:
            self.data = json.load(file)

        self.first_window = Frame(parent)
        self.first_window.grid()

        self.header_frame = Frame(self.first_window, highlightbackground="black", 
                                    highlightthickness=1, 
                                    height=60, 
                                    width=350, bg = "#F2DDC3")
        
        self.header_frame.grid(column=0, row = 0, padx=2, pady=2)
        self.header_frame.grid_propagate(0)
        self.title = Label(self.header_frame, text = "Ormiston Cafe", font = ("Royal Cresent", ), bg= "#F2DDC3")
        self.title.place(x=150,y=10)
        
        
        img1 = Label(self.header_frame, image= self.imgs.final_images[0],bg ="#F2DDC3",height=50)
        img1.image = self.imgs.final_images[0]
        img1.grid()
        img1.place(y=-4)

        self.frame2 = Frame(self.first_window, highlightbackground="black", highlightthickness=1, 
                                    height=400, 
                                    width=350, bg = "#FFFFF0")
        self.frame2.grid(row=1)
        self.frame2.grid_propagate(0)

        """Start Button"""
        self.start_button = Button(self.frame2, image=self.imgs.final_images[1], 
                            bg = "#FFFFF0", 
                            borderwidth=0, 
                            activebackground="#FFFFF0")

        self.start_button.image=self.imgs.final_images[1]
        self.start_button.grid(row=0)
        self.start_button.place(x=50)

        self.cancel_button = Button(self.frame2, image=self.imgs.final_images[2], 
                                    bg = "#FFFFF0", borderwidth=0, 
                                    activebackground="#FFFFF0")
        self.cancel_button.image=self.imgs.final_images[2]
        self.cancel_button.place(x=50,y=200)

 

"""Seperate class for images"""
class Temp_img:
    def __init__(self):

        """List of images in this secion"""
        img_list=[
            Image.open(r"Images/java-logo.png"),
            Image.open(r"Images/Start-Button.png"),
            Image.open(r"Images/cancel-button.png")              
            ]
        """list of resized images """
        img_resize = [
            img_list[0].resize((70,50), Image.ANTIALIAS), 
            img_list[1].resize((250,150), Image.ANTIALIAS),
            img_list[2].resize((250,150), Image.ANTIALIAS)    
            ]
        """List of final resized images"""
        self.final_images = [
            ImageTk.PhotoImage(img_resize[0]),
            ImageTk.PhotoImage(img_resize[1]),
            ImageTk.PhotoImage(img_resize[2])
            ]


"""main function"""
def main():
    root = Tk()
    root.title("Ormiston Cafe")
    First_window(root)
    root.resizable(0,0)
    root.mainloop()
    

main()
