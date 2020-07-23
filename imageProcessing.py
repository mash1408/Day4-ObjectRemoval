import cv2

img = cv2.imread('cricketBall.png') 
cv2.imshow('',img)
cv2.waitKey(0)

mask = cv2.imread('ball.png', 0) 
cv2.imshow('',mask)
cv2.waitKey(0)

# Performing Inpainting

telea = cv2.inpaint(img, mask, 20, cv2.INPAINT_TELEA)
# Displaying Results


cv2.imshow('',telea)
cv2.waitKey(0)

cv2.destroyAllWindows()
