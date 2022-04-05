# Import required libraries
from vidgear.gears import CamGear
from vidgear.gears import WriteGear
import cv2

# Open any valid video stream
stream = CamGear(source="my_video.mp4").start()

# Define writer with Non-compression mode and suitable output filename.
writer = WriteGear(output_filename="my_Output.mp4", compression_mode=False)

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # write frame to writer
    writer.write(frame)

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

# safely close writer
writer.close()