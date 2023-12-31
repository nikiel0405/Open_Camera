import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv.flip(frame,1)
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(2) == ord('q'):
        break
    if cv.getWindowProperty('frame', cv.WND_PROP_VISIBLE) < 1:
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()