# Import required libraries
from vidgear.gears import VideoGear
from vidgear.gears import NetGear

# Open any valid video stream.
stream = VideoGear(source="my_video.mp4").start()

# Define Netgear Server with default parameters
server = NetGear()

# loop over until KeyBoard Interrupted
while True:

    try:

        # read frames from stream
        frame = stream.read()

        # check for frame if Nonetype
        if frame is None:
            break

        # send frame to server
        server.send(frame)

    except KeyboardInterrupt:
        break

# safely close video stream
stream.stop()

# safely close server
server.close()