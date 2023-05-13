import cv2
import numpy as np

def getcontour(image, userimage):
    basecontour = contour(image)
    usercontour = contour(userimage)
    
    newimage = overlaycontours(basecontour, userimage, (0,255,0))
    finalimage = overlaycontours(usercontour, newimage, (0,0,255))

    return finalimage

def contour(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, binary = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contours

def overlaycontours(contours, userimage, color):
    for contour in contours:
        
        # BGR (blue, green, red)
        # green (uncovered)
        cv2.drawContours(userimage, [contour], -1, color, 2)
    
    return userimage

def main():

    userinp = input('What image do you want to look at: ')

    userimage = cv2.imread('assets/Metal/{}'.format(userinp))
    image = cv2.imread('assets\Metal\Metal_1.jpg')


    finalimage = getcontour(image, userimage)

    cv2.imshow('contoured', finalimage)
    cv2.waitKey(0)

main()