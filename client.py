import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 12345

def receive_message(sock):
    return sock.recv(1024).decode('utf-8')

def send_message(sock, message):
    sock.sendall(message.encode('utf-8'))

def handle_server_communication(sock):
    while True:
        server_response = receive_message(sock)
        print(server_response)
        if "Goodbye!" in server_response:
            break
        user_input = input("Your choice: ")
        send_message(sock, user_input)

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
            print(f"Connected to server at {SERVER_ADDRESS}:{SERVER_PORT}")
            handle_server_communication(client_socket)
    except ConnectionError as conn_err:
        print(f"Connection error: {conn_err}")
    except KeyboardInterrupt:
        print("\nSession ended by user.")
    finally:
        print("Client has disconnected.")

if __name__ == "__main__":
    main()
