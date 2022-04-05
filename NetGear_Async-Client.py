# Import libraries
from vidgear.gears.asyncio import NetGear_Async
import cv2, asyncio

# Define and launch Client with `receive_mode=True`
client = NetGear_Async(receive_mode=True).launch()


# Create a async function where you want to show/manipulate your received frames
async def main():
    # loop over Client's Asynchronous Frame Generator
    async for frame in client.recv_generator():
        # Show output window
        cv2.imshow("Output Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # Await before continuing
        await asyncio.sleep(0)


if __name__ == "__main__":
    # Set event loop to client's
    asyncio.set_event_loop(client.loop)
    try:
        # Run your main function task until it is complete
        client.loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        # Wait for interrupts
        pass

    # Close all output window
    cv2.destroyAllWindows()
    # Safely close client
    client.close()