# This is a sample Python script.
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PIL import Image

asciiValues = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
aDict = {}
for i in range(65):
    aDict[i] = asciiValues[i]

im = Image.open("example.jpg")
def resizeImage (image, new_width=100):
    width,height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_img = image.resize((new_width,new_height))
    return(resized_img)
im = resizeImage(im)
s1 = im.size[0]//2
s2 = im.size[1]//2
print(im.size)
print(s1,s2)

print("loaded Image")
print("Image size:",im.size)
imageList2 = list(im.getdata())
def genArrayImg(imImage):
    imageList = list(imImage.getdata())
    arrayOfPixels = []
    hozPos = 0
    verPos = 0
    for i in range(imImage.size[1]):
        arrayOfPixels.append([])
    print("generated empty 2D array for pixels, size of list:" ,len(arrayOfPixels))
    print("creating array, iterating through pixels:")
    while hozPos != imImage.size[1]:
        for i in range(imImage.size[0]):
            #print("found:" , imageList[i+verPos])
            (arrayOfPixels[hozPos]).append(imageList[i+verPos])
            #print("added:" , arrayOfPixels[hozPos][i])

        verPos += imImage.size[1]
        hozPos += 1
    print("len of array:" , len(arrayOfPixels))
    return arrayOfPixels
def avgRGB (rgblist):
    print("before",rgblist[1][1])
    hozPos = 0
    verPos = 0
    while hozPos != len(rgblist):
        for i in range((len(rgblist[1]))):
            rgblist[hozPos][i] = ((sum(rgblist[hozPos][i])) // 3)
        verPos += im.size[1]
        hozPos += 1
    print("after",rgblist[1][1])

    return rgblist

def convertToAsccii(avglist):
    print("before",avglist[1][1])
    hozPos = 0
    verPos = 0
    while hozPos != len(avglist):
        for i in range((len(avglist[1]))):
            avglist[hozPos][i] =  aDict[(int(avglist[hozPos][i])//3.92307)]
        verPos += im.size[1]
        hozPos += 1
    print("after",avglist[1][1])
    return avglist

def printImage(imgList):
    for i1 in range(len(imgList)):
        printline = ''
        for i2 in range(len(imgList[i1])):
            for i in range(3):
                printline += imgList[i1][i2]
        #print(i1)
        print(printline)




imagePixels = genArrayImg(im)
print(len(imagePixels[1]))
avgImagePixels = avgRGB(imagePixels)
avglist = convertToAsccii(avgImagePixels)
printImage(avglist)
print(aDict[64])





