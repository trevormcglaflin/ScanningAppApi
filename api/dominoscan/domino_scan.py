from .models import Domino
import cv2
import numpy as np
from matplotlib import pyplot as plt

def make_domino(pic_path):
    # initialize new domino
    domino = Domino()

    # read in image
    img = cv2.imread(str(pic_path),0)
    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    ret,thresh3 = cv2.threshold(img,100,255,cv2.THRESH_TRUNC)
    ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
    ret,thresh6 = cv2.threshold(thresh3,95,255,cv2.THRESH_BINARY)

    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh6]

    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])

    plt.savefig("blackandwhite.png")
    
    cnts = cv2.findContours(thresh3, cv2.RETR_LIST,
                    cv2.CHAIN_APPROX_SIMPLE)[-2]
    
    s1 = 2
    s2 = 200
    xcnts = []
    for cnt in cnts:
        if s1<cv2.contourArea(cnt) <s2:
            xcnts.append(cnt)
    print("\nDots number: {}".format(len(xcnts)))
    
    


    # process image
    # add top_half and bottom_half to domino


    # return domino object
    return domino



