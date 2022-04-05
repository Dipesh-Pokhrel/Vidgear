# Import required libraries
from vidgear.gears import StreamGear

# Activate Single-Source Mode with valid video input
stream_params = {"-video_source": "my_video.mp4"}
# Describe a suitable manifest-file location/name and assign params
streamer = StreamGear(output="dash_out.mpd", **stream_params)
# trancode source
streamer.transcode_source()
# terminate
streamer.terminate()