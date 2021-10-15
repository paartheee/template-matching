#import all necessary libraries
import cv2
import numpy as np

#we are using OpenCV to Get and read the Input Image
img = cv2.imread('Input path image here')

# Converts the Colored images to Grayscale Image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#we are using OpenCV to Get and read the template image
template = cv2.imread('Template image path here', 0)

#reduce the template image border
w, h = template.shape[::-1]

#Use the templete-matching function to detect the template in Input Image
#Three types of function for template matching 
#cv2.TM_SQDIFF = Template Matching Square Difference
#cv2.TM_CCOEFF = Template Matching Correlation Coefficient
#cv2.TM_CCORR  = Template Matching Cross Correlation
res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)

#set the threshold for desired output
threshold = 0.55
loc = np.where(res >= threshold)

#draw the retangle in template matched objects 
for pt in zip(*loc[::-1]):

    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

cv2.imshow ('Detected the template matching objects',img)
cv2.waitKey()
cv2.destroyAllWindows
