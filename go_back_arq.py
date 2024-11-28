import random
import time

# Function to simulate sending frames with Go-Back-N protocol
def go_back_n_protocol(window_size, total_frames):

    sent_frames = 0  # The frame currently being sent
    base = 0         # The base of the sliding window
    ack_received = [False] * total_frames  # To track acknowledgments
    timeout = 2      # Timeout in seconds

    print(f"Starting Go-Back-N Protocol with window size {window_size} and total frames {total_frames}...\n")
    
    while base < total_frames:
        # Simulate sending frames within the window
        print(f"Sending frames from {base} to {min(base + window_size - 1, total_frames - 1)}...")
        
        for i in range(base, min(base + window_size, total_frames)):
            if not ack_received[i]:
                print(f"Sent frame {i}")
        
        # Simulate acknowledgment
        time.sleep(1)  # Simulate network delay
        for i in range(base, min(base + window_size, total_frames)):
            if random.random() > 0.2:  # 80% chance of receiving ACK
                ack_received[i] = True
                print(f"ACK received for frame {i}")
            else:
                print(f"Frame {i} lost or no ACK received")
                break
        
        # Check the base of the window
        while base < total_frames and ack_received[base]:
            base += 1
        
        # Simulate timeout for lost frames
        if base < total_frames and not ack_received[base]:
            print(f"Timeout occurred for frame {base}. Resending from frame {base}...\n")
            time.sleep(timeout)
    
    print("\nAll frames sent and acknowledged successfully!")

total_frames = int(input("Enter total number of frames: "))
window_size = int(input("Enter window size: "))
go_back_n_protocol(window_size, total_frames)
