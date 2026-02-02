import cv2 as cv
# img = cv.imread("img/tree.jpg")

# cv.imshow("Display window", img)
# k = cv.waitKey(0) # Wait for a keystroke in the window

# cap = cv.VideoCapture('videos/cars.mp4')

# while True:
#   success, img = cap.read()
#   if (success):
#     cv.imshow('img', img)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#       break


cap = cv.VideoCapture(0) # camera number 0
cap.set(3, 500) # window width
cap.set(4, 300) # window height

while True:
  success, img = cap.read()
  if (success):
    cv.imshow('img', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
      break