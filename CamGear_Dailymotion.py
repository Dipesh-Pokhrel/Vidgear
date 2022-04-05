# Importing required Libraries
import cv2
from vidgear.gears import CamGear
# Setting desired quality as 720 p
resolution = {'STREAM_RESOLUTION': '720'}
# Adding any desired video URL as input source
stream = CamGear(source = 'https://www.dailymotion.com/video/x86tgq0',stream_mode = True, logging=True,**resolution).start()
# Reading frames from stream using infinite loop
while True:
    frame = stream.read()
# Checking for frame NoneType
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