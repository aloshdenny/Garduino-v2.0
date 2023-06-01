import cv2 as cv

capture = cv.VideoCapture(1)

fps = capture.get(cv.CAP_PROP_FPS)
print('frames per second =',fps)

while True:
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()