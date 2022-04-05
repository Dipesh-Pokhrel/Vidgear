# Import required libraries
from vidgear.gears import NetGear
import cv2

# Define various tweak flags
options = {"flag": 0, "copy": False, "track": False}

# Define Netgear Client at given IP address and define parameters 
client = NetGear(
    address="192.168.205.16",
    port="5353",
    protocol="tcp",
    pattern=1,
    receive_mode=True,
    logging=True,
    **options
)

# loop over
while True:

    # Receive frames from network
    frame = client.recv()

    # Check for received frame if Nonetype
    if frame is None:
        break

    
    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(4) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close client
client.close()