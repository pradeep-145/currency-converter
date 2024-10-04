import socket
import requests


def get_exchange_rate(from_currency, to_currency):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(api_url)
    data = response.json()
    return data['rates'][to_currency]

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 8090))
    print("UDP server is listening on port 8090...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(f"Connection from {client_address}")

        from_currency, to_currency, amount = data.decode().split(',')

        try:
            exchange_rate = get_exchange_rate(from_currency, to_currency)
            converted_amount = float(amount) * exchange_rate
            response = str(converted_amount)
        except Exception as e:
            response = f"Error: {str(e)}"

        server_socket.sendto(response.encode(), client_address)

if __name__ == "__main__":
    start_server()
