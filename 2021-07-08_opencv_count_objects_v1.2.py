#2021-07-08 OpenCV Count objects in picture
# v1.2
# updated image path
# pending
## Crop image or mask image automatically?

import cv2 as cv

# Accesing image

#path = '/Users/daviderubio/Desktop/Python_stuff/environments/env_2/images/count7.jpg'
path = '/Users/daviderubio/Desktop/Python_stuff/environments/env_2/images/2021-07-08_count_test_raspi_2_cropped.jpg'

image = cv.imread(path)

# Resize Image 

scale_percent = 30 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv.resize(image, dim, interpolation = cv.INTER_AREA)

# Image Processing Functions

gray = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
#blur = cv.bilateralFilter(gray, 13, 75, 75)
blur0 = cv.GaussianBlur(gray,(5,5),0)
blur = cv.GaussianBlur(blur0,(5,5),0)
#edges = cv.Canny(blur, 350,5)
edges = cv.Canny(blur, 30,5)

# Count number of objects
contours, hierarchy = cv.findContours(edges.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
number_of_objects_in_image = len(contours)

# Print number of objects
print ("The number of objects in this image: ", str(number_of_objects_in_image))


# Display processed images

cv.imshow("image", resized)
cv.waitKey(0)

cv.imshow("gray", gray)
cv.waitKey(0)

cv.imshow("blur", blur)
cv.waitKey(0)

cv.imshow("edges", edges)
cv.waitKey(0)

cv.destroyAllWindows()
