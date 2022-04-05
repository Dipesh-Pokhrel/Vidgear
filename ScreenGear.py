# Importing required library
import cv2
from vidgear.gears import ScreenGear

# Opening any valid stream.
stream = ScreenGear().start()
# Reading frames from stream using infinite loop
while True:
    frame = stream.read()
# Checking for frame NoneType
    if frame is None:
        break
# Showing the output window.
    cv2.imshow('Output_frame', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
# Cloasing output window.
cv2.destroyAllWindows()
# Safely closing video stream
stream.stop()
