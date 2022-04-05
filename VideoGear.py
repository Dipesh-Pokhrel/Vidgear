# Import Required library
from vidgear.gears import VideoGear
import numpy as np 
import cv2
# Open any valid stream with stabilization enabled.
stream_stab = VideoGear(source='my_video.mp4',stabilize=True).start()
# Open same valid stream without stabilization.
stream_org = VideoGear(source='my_video.mp4').start()

while True:
    # Read stabilized frame
    frame_stab = stream_stab.read()
    # Check stabilized frame
    if frame_stab is None:
        break
    # Read unstabilized frame
    frame_org = stream_org.read()
    # Conctaenate both frames
    output_frame = np.concatenate((frame_org,frame_stab),axis=1)
    # Put text over concatenated frame
    cv2.putText(output_frame,'Before',(10,output_frame.shape[0]-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
    cv2.putText(output_frame,'After',(output_frame.shape[1]//2+10,output_frame.shape[0]-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
    # Show output window
    cv2.imshow('my_stream',output_frame)
    # Check for 'q' key if pressed.
    key = cv2.waitKey(15) & 0xFF 
    if key == ord('q'):
        break
    # Close output window
    cv2.destroyAllWindows()
    # Safe closing of both streams.
    stream_org.stop()
    stream_stab.stop()