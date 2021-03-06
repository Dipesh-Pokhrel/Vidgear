# Import required libraries
from vidgear.gears import NetGear
import cv2


# Define Netgear Client with `receive_mode = True` and default parameter
client = NetGear(receive_mode=True)

# loop over
while True:

    # receive frames from network
    frame = client.recv()

    # check for received frame if Nonetype
    if frame is None:
        break


    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(5) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close client
client.close()