# opencv-learn

### Inspiration
[OpenCV: Как Начать Работать с Компьютерным Зрением // Демо-занятие курса «Компьютерное зрение»](https://vkvideo.ru/video-145052891_456247174)

### Create
```bash
python3 -m venv myvenv
```

### Activate
```bash
source myvenv/bin/activate
```

### Deactivate
```bash
deactivate
```

### install opencv
```bash
pip3 install opencv-python numpy matplotlib mediapipe
```

### Example code
```python
import cv2 as cv
img = cv.imread("path/to/image")

cv.imshow("Display window", img)
k = cv.waitKey(0) # Wait for a keystroke in the window
```