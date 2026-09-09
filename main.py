from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import os


# Remember Box: Widgets always need a position (For Example:".place" or ".pack"), Frames are containers, you may put a frame inside another frame. By making the original frame the parent

Photo = None
Sidebar_button_1_label = None

# A Photo List

Photo_list = []

# Event for starting the dragging of the image.

def Drag_that_damn_image(event):
        Drag = event.widget
        Drag.startX = event.x
        Drag.startY = event.y

# Event for dragging the image around the screen.

def KEEP_DRAGGING(event):
         Drag = event.widget
         x = Drag.winfo_x() - Drag.startX + event.x
         y = Drag.winfo_y() - Drag.startY + event.y
         Drag.place(x=x, y=y)


# To add a reference image to the screen.

def showref():
    global Photo, Sidebar_button_1_label
    Photos = filedialog.askopenfilename(initialdir= os.getcwd(), filetypes= (("JPG file", "*.jpg"),
                                        ("PNGFile", "*.png") ,("All Files", "*.*")))
    
    Photo = Image.open(Photos)
    Photo.thumbnail((300,300))
    Reference = ImageTk.PhotoImage(Photo)
    Sidebar_button_1_label= Label(Screen_1_canvas)
    Sidebar_button_1_label.place(x=300, y=0)
    Sidebar_button_1_label.config (image=Reference)
    Sidebar_button_1_label.image= Reference

    Sidebar_button_1_label.Photo = Photo

    Sidebar_button_1_label.bind("<Control-Button-1>", start_resize)
    Sidebar_button_1_label.bind("<Control-B1-Motion>", dynamic_resize)
    Sidebar_button_1_label.bind("<Button-1>", Drag_that_damn_image)
    Sidebar_button_1_label.bind("<B1-Motion>", KEEP_DRAGGING)
     
     
    for x in range(1000):
       
     Photo_list.append(Photo)

def start_resize(event):
        Resize = event.widget
        global start_width, start_height, start_mouse_x, start_mouse_y, Sidebar_button_1_label
        start_mouse_x = event.x_root
        start_mouse_y = event.y_root
        start_width = Resize.Photo.width
        start_height = Resize.Photo.height

def dynamic_resize(event):
        Resize = event.widget
        global Photo, Sidebar_button_1_label
        distance_x = event.x_root - start_mouse_x
        distance_y = event.y_root - start_mouse_y
        new_width = max(10, start_width + distance_x)
        new_height = max(10, start_height + distance_y)
        Resizing_Image = Resize.Photo.resize((new_width, new_height))
        Bling_Blong = ImageTk.PhotoImage(Resizing_Image)
        Resize.config(image=Bling_Blong)
        Resize.image = Bling_Blong

# Textbox, to add a textbox to the screen.
 
def showtext():
    Textbox = Entry(Screen_1, width= 30, font=("Times", 10))
    Textbox.place(x=300, y=400)
    Textbox.bind("<Button-1>", Drag_that_damn_image)
    Textbox.bind("<B1-Motion>", KEEP_DRAGGING)

# Mainscreen and text on top.

Pileup = Tk()
Pileup.title("Pileup")
Pileup.state("zoomed")
Pileup.rowconfigure(0, weight=1)
Pileup.columnconfigure(0, weight=1)
Pileup.iconbitmap("C:/Users/PMYLS/Downloads/Button_Image_2.ico")
Pileup.bg= "#4A2928"
Pileup_font = Font(family="Pileup", size=60)
Pileup_text = Label(
                    Pileup, text="A Wizard's Secret Stash.", 
                    font=("Pileup", 60),
                    bg=("#4A2928"),
                    bd="0",
                    fg=("white"))

# Frames

Pileup_mainscreen = Frame(Pileup)
Pileup_mainscreen_label = Label(Pileup_mainscreen,
                    bg=("#4A2928"),
                    font= ("Pileup", 60),
                    text= "A Wizard's Secret Stash.",
                    fg=("white"),
)
Pileup_mainscreen_label.place(x=350, y=0)

Screen_1 = Frame(Pileup)

# Frames' functions

for frame in (Screen_1, Pileup_mainscreen):
        frame.grid(row=0,column=0,sticky="nsew")

def show_frame(frame):
        frame.tkraise()
        
show_frame(Pileup_mainscreen)

# Screen_1 Canvas
Screen_1_canvas = Canvas(Screen_1, bd="0")
Screen_1_canvas.place(x=0, y=0, width=7000, height=7000)

 # Screen_1_label

Screen_1_label= Label(
        Screen_1,
        text="",
        font=("Pileup", 70),
        fg=("#4A2928"))
Screen_1_label.place(x=150, y=100)

# Sidebar Frame inside Screen_1

Sidebar_frame = Frame(
              Screen_1,
              bg="#D6D6D6",
              width= "150",
              height="700")

Sidebar_frame.grid(row=0,column=0,sticky="w")

# Sidebar Buttons inside the Sidebar Frame

Sidebar_button_1 = Button(
                Sidebar_frame,
                text="Add Reference",
                font=("Pileup", 20),
                fg="Black",
                command=showref,
                bg="white",)
Sidebar_button_1.place(x=10, y=50)

# Sidebar Button 2

Sidebar_button_2 = Button(
                Sidebar_frame,
                text="Add Textbox",
                font=("Pileup", 20),
                fg="Black",
                command=showtext,
                bg="white",)
Sidebar_button_2.place(x=10, y=200)


# Background Image

Background = Image.open("Background.png")
Background = ImageTk.PhotoImage(Background)


Background_text = Label(
                    Pileup_mainscreen,
                    image=Background,
                    bd="0",
                    text="")
                    
Background_text.place(x=0, y=0)

Button_Image_1 = Image.open("Button_Image_1.png").resize((400,400))
Button_Image_1 = ImageTk.PhotoImage(Button_Image_1)

# New Board Button, along with the image it is supposed to display.

New_board_button = Button(
                       Pileup_mainscreen, 
                       image=Button_Image_1,
                       text="",
                       command=lambda:show_frame(Screen_1),
                       font=("Pileup", 60), 
                       bg="#4A2928", 
                       fg="red",
                       bd="0",
                       activebackground="#4A2928",
                       foreground="#4A2928",
                       )

# Text for the New Board button

New_board_text = Label(
    Pileup_mainscreen,
    text="New Board",
    font=("Pileup", 70),
    bg="#4A2928", 
     fg="#7659A6",
)
New_board_text.place(x=525, y=560)


# For positions, title and the mainloop of the project.

New_board_button.place(x=450, y=150)
Background_text.lower()
Pileup_text.place(x=350, y=0)
Pileup.mainloop()

