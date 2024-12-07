import socket
import threading
import requests
import json

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345
API_KEY = '9d9b66c1e4e04b8a85656fae87e7f1b1'

def fetch_data(request_type, filters=None):
    url = "https://newsapi.org/v2/"
    endpoints = {"headlines": "top-headlines", "sources": "sources"}
    params = {"apiKey": API_KEY}
    if filters:
        params.update(filters)
    try:
        response = requests.get(url + endpoints[request_type], params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        return {"error": str(error)}

def handle_client(sock, address):
    client_name = None
    try:
        sock.send("Welcome! Please enter your name: ".encode('utf-8'))
        client_name = sock.recv(1024).decode('utf-8').strip()
        while True:
            main_menu = """
            Main Menu:
            1. Search Headlines
            2. View Sources
            3. Exit
            Enter your choice: """
            sock.send(main_menu.encode('utf-8'))
            choice = sock.recv(1024).decode('utf-8').strip()
            if choice == "1":
                headlines_menu = """
                Headlines Menu:
                1. Search by Keyword
                2. Search by Category
                3. Search by Country
                4. List All Headlines
                5. Back to Main Menu
                Enter your choice: """
                sock.send(headlines_menu.encode('utf-8'))
                sub_choice = sock.recv(1024).decode('utf-8').strip()
                filters = {}
                if sub_choice in ["1", "2", "3"]:
                    sock.send("Enter value: ".encode('utf-8'))
                    value = sock.recv(1024).decode('utf-8').strip()
                    filters = {"1": {"q": value}, "2": {"category": value}, "3": {"country": value}}.get(sub_choice, {})
                results = fetch_data("headlines", filters)
                file_name = f"{client_name}_headlines.json"
                with open(file_name, "w") as file:
                    json.dump(results, file)
                sock.send(f"Headlines saved to {file_name}\n".encode('utf-8'))
            elif choice == "2":
                sources_menu = """
                Sources Menu:
                1. Filter by Category
                2. Filter by Country
                3. Filter by Language
                4. View All Sources
                5. Back to Main Menu
                Enter your choice: """
                sock.send(sources_menu.encode('utf-8'))
                sub_choice = sock.recv(1024).decode('utf-8').strip()
                filters = {}
                if sub_choice in ["1", "2", "3"]:
                    sock.send("Enter value: ".encode('utf-8'))
                    value = sock.recv(1024).decode('utf-8').strip()
                    filters = {"1": {"category": value}, "2": {"country": value}, "3": {"language": value}}.get(sub_choice, {})
                results = fetch_data("sources", filters)
                file_name = f"{client_name}_sources.json"
                with open(file_name, "w") as file:
                    json.dump(results, file)
                sock.send(f"Sources saved to {file_name}\n".encode('utf-8'))
            elif choice == "3":
                sock.send("Goodbye!\n".encode('utf-8'))
                break
            else:
                sock.send("Invalid choice. Try again.\n".encode('utf-8'))
    finally:
        sock.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((SERVER_HOST, SERVER_PORT))
        server_socket.listen(5)
        while True:
            client_sock, client_addr = server_socket.accept()
            threading.Thread(target=handle_client, args=(client_sock, client_addr)).start()

if __name__ == "__main__":
    start_server()
