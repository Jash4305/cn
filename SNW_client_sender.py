import socket
import time

def main():
    host = '127.0.0.1'
    port = 12345
    timeout = 4  # Timeout in seconds for receiving ACK
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    total_frames = int(input("Enter total number of frames to send: "))
    client_socket.send(str(total_frames).encode())
    
    frame_number = 1

    while frame_number <= total_frames:
        print(f"Sending Frame {frame_number}")
        client_socket.send(str(frame_number).encode())
        
        start_time = time.time()  # Start timer for ACK
        
        while True:
            try:
                client_socket.settimeout(timeout)  # Set timeout for ACK
                response = client_socket.recv(1024).decode()
                
                if response == "ACK":
                    print(f"Frame {frame_number} acknowledged by server.")
                    frame_number += 1
                    break  # Move to the next frame
                else:
                    print(f"Frame {frame_number} not acknowledged. Retrying...")
                    time.sleep(1)
                    print(f"Resending Frame {frame_number}")
                    client_socket.send(str(frame_number).encode())
            
            except socket.timeout:
                print(f"Timeout for Frame {frame_number}. Resending...")
                client_socket.send(str(frame_number).encode())  # Resend the frame
                start_time = time.time()  # Reset timer

    print("All frames sent successfully!")
    client_socket.close()


if __name__ == "__main__":
    main()
