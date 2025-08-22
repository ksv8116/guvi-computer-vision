import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images.jpeg")
print(img.shape)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGBn ))
plt.show()