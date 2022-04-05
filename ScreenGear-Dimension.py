# import required libraries
from vidgear.gears import ScreenGear
import cv2

# Define dimensions of screen w.r.t to given monitor to be captured
options = {"top": 40, "left": 0, "width": 100, "height": 100}

# open video stream with defined parameters
stream = ScreenGear(logging=True, **options).start()

# loop over
while True:

    # Read frames from stream
    frame = stream.read()

    # Check for frame if Nonetype
    if frame is None:
        break


    # Show output window
    cv2.imshow("Output Frame", frame)

    # Check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Close output window
cv2.destroyAllWindows()

# Safely close video stream
stream.stop()