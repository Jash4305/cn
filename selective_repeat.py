import random
import time

# Function to simulate sending frames with Selective Repeat protocol
def selective_repeat_protocol(window_size, total_frames):

    # Initialize variables
    sent_frames = [False] * total_frames  # Track which frames have been sent
    ack_received = [False] * total_frames  # Track which frames have been acknowledged
    timeout = 2  # Timeout in seconds
    timer = [None] * total_frames  # Timer for each frame
    frame_status = ["Not Sent"] * total_frames  # For logging frame status

    print(f"Starting Selective Repeat Protocol with window size {window_size} and total frames {total_frames}...\n")

    base = 0  # Base of the window

    while base < total_frames:
        # Send frames within the current window
        for i in range(base, min(base + window_size, total_frames)):
            if not sent_frames[i]:
                print(f"Sent frame {i}")
                sent_frames[i] = True
                timer[i] = time.time()  # Start timer for the frame
                frame_status[i] = "Sent"

        # Simulate acknowledgment for frames in the window
        time.sleep(1)  # Simulate network delay
        for i in range(base, min(base + window_size, total_frames)):
            if not ack_received[i]:
                if random.random() > 0.2:  # 80% chance of ACK
                    ack_received[i] = True
                    print(f"ACK received for frame {i}")
                    frame_status[i] = "Acknowledged"
                else:
                    print(f"Frame {i} lost or no ACK received")
                    frame_status[i] = "Lost"

        # Retransmit frames with expired timers or no ACK
        for i in range(base, min(base + window_size, total_frames)):
            if not ack_received[i]:
                if time.time() - timer[i] >= timeout:
                    print(f"Timeout for frame {i}. Resending...")
                    print(f"Sent frame {i} again")
                    timer[i] = time.time()  # Reset the timer

        # Slide the window for acknowledged frames
        while base < total_frames and ack_received[base]:
            base += 1

        print("\nWindow Status:")
        for i in range(total_frames):
            print(f"Frame {i}: {frame_status[i]}")
        print()

    print("\nAll frames sent and acknowledged successfully!")


# Driver Code
if __name__ == "__main__":
    total_frames = int(input("Enter total number of frames: "))
    window_size = int(input("Enter window size: "))
    selective_repeat_protocol(window_size, total_frames)
