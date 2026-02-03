import cv2
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

WINDOW_WIDTH_PROP = 3

cap = cv2.VideoCapture(0) # camera number 0
# cap.set(WINDOW_WIDTH_PROP = 3, 500) # window width
# cap.set(4, 300) # window height

face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
  success, frame = cap.read()
  fps = cap.get(cv2.CAP_PROP_FPS)
  cv2.putText(
    frame,
    str(fps),
    (20, 30),
    fontFace=cv2.FONT_HERSHEY_COMPLEX,
    fontScale=1,color=(0, 255, 0)
  )
  if (success):
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade_db.detectMultiScale(gray_frame, 1.1, 19)
    for (x, y, w, h) in faces:
      cv2.rectangle(frame, (x, y), (x + w, y + w), (0, 255, 0), 2)
    cv2.imshow('frame', frame)

cap.release()
cv2.destroyAllWindows()