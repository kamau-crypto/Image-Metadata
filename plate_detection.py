#
# Import the Needed dependencies
import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr
#
# Read the Image, Grayscale, and Blur it
img= cv2.imread('./src/1666187493262.jpg')
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(cv2.cvtColor(gray,cv2.COLOR_BAYER_BG2BGR))
#
# Filter and find edges for localization
#
# Find Contours and Apply Mask
#
# Use Easy OCR to read text
#
# Render the results