# Import required libraries
from vidgear.gears import CamGear
from vidgear.gears import StreamGear
import cv2

# Open any valid video stream
stream = CamGear(source='my_video.mp4').start() 

# Describe a suitable manifest-file location/name
streamer = StreamGear(output="dash_out1.mpd")

# loop over
while True:

    # Read frames from stream
    frame = stream.read()

    # Check for frame if Nonetype
    if frame is None:
        break

    # Send frame to streamer
    streamer.stream(frame)

    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()

# safely close streamer
streamer.terminate()