import cv2
print(cv2.__version__)
import numpy as np
import matplotlib.pyplot as plt

# Read the image

image = cv2.imread("1.png")

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# image_rgb[:,:,0] = 0
image_rgb[:,:,1] = 0
image_rgb[:,:,2] = 0
plt.imshow(image_rgb)

plt.show()