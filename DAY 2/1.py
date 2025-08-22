import cv2
import matplotlib.pyplot as plt

img = cv2.imread("imagess.jpeg")
rows,cols=img.shape[:2]
(h,w) = img.shape[:2]

cv2.flip(img,1)

print(img.shape)

cv2.circle(img,(50,50),60,(0,0,255),1)

RM = cv2.getRotationMatrix2D((w//2,h//2),45,1)
rotated = cv2.warpAffine(img,RM,(w,h))

plt.imshow(cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB))
plt.show()