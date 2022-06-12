"""Modules used"""
from tkinter import*
from tkinter import ttk
import json
from PIL import ImageTk,Image

"""Class for the program's interface""" 
class App:
    def __init__(self, parent):

        """connecting the image class to the interface class"""
        self.imgs = Data()

        """Loads json database"""
        with open("Data.json", "r") as file:
            self.database = json.load(file)

        """First window frame is created"""
        self.main_window = Frame(parent)
        self.main_window.grid()

        self.header_frame = Frame(self.main_window, highlightbackground="black", 
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

        self.frame2 = Frame(self.main_window, highlightbackground="black", highlightthickness=1, 
                                    height=400, 
                                    width=350, bg = "#FFFFF0")
        self.frame2.grid(row=1)
        self.frame2.grid_propagate(0)

        """Start Button created"""
        self.start_button = Button(self.frame2, image=self.imgs.final_images[1], 
                            bg = "#FFFFF0", 
                            borderwidth=0, 
                            activebackground="#FFFFF0",
                            command=self.start)

        self.start_button.image=self.imgs.final_images[1]
        self.start_button.grid(row=0)
        self.start_button.place(x=50)

        """Cancel button created"""
        self.cancel_button = Button(self.frame2, image=self.imgs.final_images[2], 
                                    bg = "#FFFFF0", borderwidth=0, 
                                    activebackground="#FFFFF0")
        self.cancel_button.image=self.imgs.final_images[2]
        self.cancel_button.place(x=50,y=200)


    def start(self):
        """removes frame 2"""
        self.frame2.grid_forget()
        
        self.title.place(x=90,y=10)
    
        """creates selection frame"""
        self.selection_frame = Frame(self.main_window,highlightbackground="black", highlightthickness=1, 
                                    height=400, 
                                    width=350, bg = "#FFFFF0")
        self.selection_frame.grid(row=2)
        self.selection_frame.grid_propagate(0)

        self.menu_frame = Frame(self.main_window,highlightbackground="black",highlightthickness= 1,
                                height=40, width=350,
                                bg = "#A79280")
        self.menu_frame.grid(row=1)
        

        for self.i in range(len(self.imgs.menu_list)):
            Button(self.menu_frame, text = self.imgs.menu_list[self.i], bg = "white").grid(column= self.i, 
                    row=0, padx= 15, pady = 5)

        self.menu_button = Button(self.header_frame, text = "Main Menu",bg = "white",
                            command = self.back)
        self.menu_button.place(x = 250, y=10)
        self.menu_frame.grid_propagate(0)

    def back(self):
        self.selection_frame.grid_forget()
        self.menu_frame.grid_forget()
        self.menu_button.destroy()
        self.frame2.grid()



   

"""class for images"""
class Data:
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
        """List of button names"""
        self.menu_list = ['Sandwitches', 'Sides','Desserts','Drinks']


"""main function"""
def main():
    root = Tk()
    root.title("Ormiston Cafe")
    App(root)
    root.resizable(0,0)
    root.mainloop()

main()
