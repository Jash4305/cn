import socket
import random
import time

host = '127.0.0.1'
port = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print("Server is waiting for a connection...")
conn, addr = server_socket.accept()
print(f"Connection established with {addr}")

total_frames = int(conn.recv(1024).decode())
print(f"Total frames to receive: {total_frames}")

received_frame = 0

while received_frame < total_frames:
    frame = conn.recv(1024).decode()
    print(f"Received Frame: {frame}")

    # Simulate random delay or lost ACKs
    if random.choice([True, False]):
        print(f"Sending ACK for Frame {frame}")
        conn.send("ACK".encode())
        received_frame += 1
    else:
        print(f"Simulating lost ACK for Frame {frame}. Sending NACK.")
        time.sleep(2)  # Simulate delay in sending response
        conn.send("NACK".encode())

print("All frames received successfully!")
conn.close()
server_socket.close()
