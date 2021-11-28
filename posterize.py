"""

File:posterize.py
Project 7.5
Defines and tests a function for posterizing images.

"""
from images import Image

def posterize(image, color = (0,0,0)):
    """ Converts a color image to two colors"""
    whitePixel = (255, 255,255)
    """uses loop to manipulate the image """
    for y in range (image.getHeight()):
        """ nested loop for x and y """
        for x in range(image.getWidth()):
            (r,g,b) = image.getPixel(x,y)
            average = (r + g + b) // 3
            """ divide by number of values -- in this case 3"""
            if average < 128:
                image.setPixel(x,y, color)
            else:
                    image.setPixel(x,y, whitePixel)
def  main():
    filename = input("Enter the image file name:  ")
    red = int(input("Enter an integer [0..255] for red: "))
    green = int(input(" Enter an integer [0..255] for green : "))
    blue = int(input(" Enter an integer [0..255] for blue : " ))
    image = Image(filename)
    posterize(image,(red,green,blue))
    image.draw()

if __name__ == "__main__":
    main()
    
