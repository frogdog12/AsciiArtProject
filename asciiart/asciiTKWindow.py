# Kinter testing grounds for Ascii project
import tkinter
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

#ASCII CODE
#generate a dict of ascii to use to assign to each pixel
asciiValues = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
aDict = {}
for i in range(65):
    aDict[i] = asciiValues[i]


def resizeImage (image, new_width):
    #Take in an image, and resizes image to set width, while maintaining aspect ratio
    width,height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_img = image.resize((new_width,new_height))
    return(resized_img)

#creates list of pixels, and averges the RGB values
def image_pixels_list(image):
    imageList = list(image.getdata())
    for i in range(len(imageList)):
        #print("before: ", imageList[i])
        imageList[i] = ((sum(imageList[i])) // 3)
        #print("after: ", imageList[i])
    return imageList

#Converts avg RGB values to ascii based on ascii DICT
def image_list_convert_to_ascii(avglist):
    for i in range(len(avglist)):
        #print("before: ", avglist[i])
        avglist[i] = aDict[(int(avglist[i]) // 3.984375)]

        #print("after: ", avglist[i])
    return avglist

def create_2d_array(ascii_list,image):
    #creates a 2d array, with dimensions based on size of original image
    imageDim = image.size
    imgArray = [["" for i in range(imageDim[0])] for j in range(imageDim[1])]
    counter = 0
    for i in range(len(imgArray)):
        for j in range(len(imgArray[i])):
            imgArray[i][j] = ascii_list[counter]
            counter+=1


    return imgArray

# def print_ascii(alist):
#     #prints ascii using the 2d array given
#     for i in range(len(alist)):
#         println = ''
#         for j in range(len(alist[i])):
#             for k in range(3):
#                 println += alist[i][j]
#         print(println)

def list_to_string(alist):
    output = ''
    for i in range(len(alist)):
        for j in range(len(alist[i])):
            for k in range(2):
                output += alist[i][j]
        output+=('\n')
    return output


def cornSeed(im):
    im = resizeImage(im,200)
    ImList = image_pixels_list(im)
    AsciiList = image_list_convert_to_ascii(ImList)
    imagearray = create_2d_array(AsciiList, im)
    imagestr = list_to_string(imagearray)
    return imagestr




root = Tk()
root.minsize(500,600)
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
        file_path

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
    a_label.config(text=file_path)
    image_label.photo = photo



def submit():
    width = w_size.get()
    clear_screen()
    im = cornSeed(Image.open(a_label.cget("text")))
    a_label.config(text=im)
    a_label.grid(row=0,column=0)
    # ascii_text.insert(INSERT,im)
    # ascii_text.grid(row=0,column=0)


def clear_screen():
    #clears or restores labels
        if image_label.grid_info() != {}:
            image_label.grid_remove()
            open_button.grid_remove()
            width_label.grid_remove()
            #height_label.grid_remove()
            width_entry.grid_remove()
            #height_entry.grid_remove()
            go_btn.grid_remove()
        else:
            image_label.grid()
            open_button.grid()
            width_label.grid()
            #height_label.grid()
            width_entry.grid()
            #height_entry.grid()
            go_btn.grid()

#ASCII test label?
# a_label = tkinter.Label(frame,text='',font=("TkFixedFont ",6),justify=LEFT,)

a_label = tkinter.Label(frame,justify=LEFT, text='',font=('courier',2))

#ascii text trial
ascii_text = tkinter.Text(font=("TkFixedFont",4),height=500,width=500)

# button for opening image
open_button = tkinter.Button(frame, text="open image", command=open_image, height=1, width=20)
open_button.grid(row=1, column=0, columnspan=2)

# Label used for displaying image
image_label = tkinter.Label(frame)
display_image("black.png")
image_label.grid(row=0, column=0)

# Label for size inputs
width_label = tkinter.Label(input_Frame, text="ASCII Image Width:", justify="left", anchor="w")
#height_label = tkinter.Label(input_Frame, text="ASCII Image Height:",justify="left", anchor="w")
width_label.grid(row=0, column=0)
#height_label.grid(row=1, column=0)


# input boxes for sizes
width_entry = tkinter.Entry(input_Frame, textvariable= w_size)
# height_entry = tkinter.Entry(input_Frame, textvariable=h_size)
width_entry.grid(row=0, column=1)
# height_entry.grid(row=1, column=1)
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

