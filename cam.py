import cv2 as cv
cap= cv.VideoCapture(0)
while True:
    ret, frame = cap.read()
    resized = cv.resize(frame, (600, 400))
    cv.imshow('frame', resized)


    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
