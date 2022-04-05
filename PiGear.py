import cv2
from vidgear.gears import PiGear
# Opening PI video stream from default parameter 
stream = PiGear().start()

while True:
# reading frame from stream.
    frame = stream.read()
# Checking for frame
    if frame is None:
        break
# Showing the output window.
    cv2.imshow('My_video', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
# Cloasing output window.
cv2.destroyAllWindows()
# Safely closing video stream
stream.stop()
