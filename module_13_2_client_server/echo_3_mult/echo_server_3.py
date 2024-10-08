import socket
import threading

HOST = "127.0.0.1"
PORT = 50131


def handle_connection(sock, addr):
    with sock:
        print("Подключение по", addr)
        while True:
            # Recieve
            try:
                data = sock.recv(1024)
            except ConnectionError:
                print("Клиент внезапно отключился в процессе отправки данных на сервер")
                break
            print(f"Получено: {data}, from: {addr}")
            data = data.upper()
            # Send
            print(f"Send: {data} to: {addr}")
            try:
                sock.sendall(data)
            except ConnectionError:
                print(f"Клиент внезапно отключился не могу отправить данные")
                break
        print("Отключение по", addr)


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_sock:
        serv_sock.bind((HOST, PORT))
        serv_sock.listen(1)
        while True:
            print("Ожидаю подключения....")
            sock, addr = serv_sock.accept()
            thread = threading.Thread(target=handle_connection, args=(sock, addr))
            print(thread)
            thread.start()
