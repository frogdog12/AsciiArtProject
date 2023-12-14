# Kinter testing grounds for Ascii project
import tkinter
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk


root = Tk()
root.minsize(300,500)
frame = Frame(root)
input_Frame = tkinter.Frame(frame)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# create height and width vars
h_size = tkinter.StringVar()
w_size = tkinter.StringVar()


def open_image():
    # opens image to be converted/displayed
    file_path = filedialog.askopenfilename(title="Open Image to convert",
                                           filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])
    if file_path:
        display_image(file_path)


def resize_thumb(image):
    # computes ratio for image, and converts to have a width of 100
    imageWidth, imageHeight = image.size
    newHeight = int(imageHeight // (imageWidth / 200))
    image = image.resize((200, newHeight))
    return image


def display_image(file_path):
    # sets image label to image, and displays
    image = Image.open(file_path)
    image = resize_thumb(image)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.photo = photo


def submit():
    height = h_size.get()
    width = w_size.get()
    clear_screen()
    print("The name is : " + height)
    print("The password is : " + width)

    h_size.set("")
    w_size.set("")

def clear_screen():
    #clears or restores labels
        if image_label.grid_info() != {}:
            image_label.grid_remove()
            open_button.grid_remove()
            width_label.grid_remove()
            height_label.grid_remove()
            width_entry.grid_remove()
            height_entry.grid_remove()
        else:
            image_label.grid()
            open_button.grid()
            width_label.grid()
            height_label.grid()
            width_entry.grid()
            height_entry.grid()


# button for opening image
open_button = tkinter.Button(frame, text="open image", command=open_image, height=1, width=20)
open_button.grid(row=1, column=0, columnspan=2)

# Label used for displaying image
image_label = tkinter.Label(frame)
display_image("black.png")
image_label.grid(row=0, column=0)

# Label for size inputs
width_label = tkinter.Label(input_Frame, text="ASCII Image Width:", justify="left", anchor="w")
height_label = tkinter.Label(input_Frame, text="ASCII Image Height:",justify="left", anchor="w")
width_label.grid(row=0, column=0)
height_label.grid(row=1, column=0)


# input boxes for sizes
width_entry = tkinter.Entry(input_Frame, textvariable= w_size)
height_entry = tkinter.Entry(input_Frame, textvariable=h_size)
width_entry.grid(row=0, column=1)
height_entry.grid(row=1, column=1)
input_Frame.grid(row=2,column=0)

#go button
go_btn = tkinter.Button(frame, text="Go",command=submit)
go_btn.grid(row=6,column =0, columnspan=2)






rows = 6
columns = 2

for i in range(rows):
    root.grid_rowconfigure(i,weight=1)
for i in range(columns):
    root.grid_columnconfigure(i,weight=1)

root.mainloop()

