import cv2
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [6, 4]

img = cv2.imread("img/tree.jpg", cv2.IMREAD_COLOR)

cv2.imshow("Display window", img)
cv2.waitKey(1000) # Wait for a keystroke in the window
print(img.shape) # (354, 236, 3) => (width, height, channels)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", img_gray)
cv2.waitKey(1000) # Wait for a keystroke in the window

color = ('b', 'g', 'r')
for i, col in enumerate(color):
  histogram = cv2.calcHist([img], [i], None, [256], [0, 256])
  plt.plot(histogram, color = col)
  plt.xlim([0,256])
plt.title('Histogram for RGB by OpenCV')
plt.show()