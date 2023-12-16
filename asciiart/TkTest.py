import tkinter as tk
from tkinter import filedialog, BOTTOM, LEFT
from tkinter import *
from PIL import Image, ImageTk
def open_image():
    file_path = filedialog.askopenfilename(title="Select Image to Convert", filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])
    if file_path:
        display_image(file_path)
def display_image(file_path):
    image = Image.open(file_path)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.photo = photo

#sets up TK window
root = tk.Tk()
root.title("Ascii Art Generator")
fm = Frame(root)
# root.state('zoomed')
size_var = tk.IntVar()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

open_button = tk.Button(fm, text="Open Image", command=open_image)
size_ent = tk.Entry(fm, relief="groove")
size_label = tk.Label(fm, text="Enter Size:")

open_button.grid(row=0, column=0, pady = 2)
size_ent.grid(row=1, column=1, pady = 2)
size_label.grid(row=1, column=0, pady = 2)
image_label = tk.Label(fm)
image_label.grid(row=1, column=1,pady = 2)
fm.pack()
root.mainloop()