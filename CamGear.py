# Importing required library
import cv2
from vidgear.gears import CamGear

# Opening any valid stream.
stream = CamGear(source = 'my_video.mp4').start()
# Reading frames from stream using infinite loop
while True:
    frame = stream.read()
# Checking for frame NoneType
    if frame is None:
        break
# Showing the output window.
    cv2.imshow('My_video', frame)
    key = cv2.waitKey(5) & 0xFF
    if key == ord('q'):
        break
# Cloasing output window.
cv2.destroyAllWindows()
# Safely closing video stream
stream.stop()
