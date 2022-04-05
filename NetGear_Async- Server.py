# Import libraries
from vidgear.gears.asyncio import NetGear_Async
import asyncio

# Initialize Server with suitable source
server = NetGear_Async(source="my_video.mp4").launch()

if __name__ == "__main__":
    # Set event loop
    asyncio.set_event_loop(server.loop)
    try:
        # Run your main function task until it is complete
        server.loop.run_until_complete(server.task)
    except (KeyboardInterrupt, SystemExit):
        # Wait for interrupts
        pass
    finally:
        # Finally close the server
        server.close()