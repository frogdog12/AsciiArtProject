from PIL import Image


#Selects image to use
im = Image.open("zebra.jpg")

#generate a dict of ascii to use to assign to each pixel
asciiValues = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
aDict = {}
for i in range(65):
    aDict[i] = asciiValues[i]


def resizeImage (image, new_width=50):
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

def print_ascii(alist):
    #prints ascii using the 2d array given
    for i in range(len(alist)):
        println = ''
        for j in range(len(alist[i])):
            for k in range(3):
                println += alist[i][j]
        print(println)

def cornSeed(im):
    ImList = image_pixels_list(im)
    AsciiList = image_list_convert_to_ascii(ImList)
    imagearray = create_2d_array(AsciiList, im)
    return imagearray

imagearray = cornSeed(im)
print_ascii(imagearray)



