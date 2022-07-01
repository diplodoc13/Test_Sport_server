import socket
from datetime import datetime

log_file = 'log.txt'
bind_ip = "localhost"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


server.listen(5)
print("Server listening on {}:{}".format(bind_ip, bind_port))

try:
    while True:
        client_socket, address = server.accept()
        received_data = client_socket.recv(1024).decode("utf-8")
        tmp = received_data.split(" ")
        printing_data = f"Спортсмен, нагрудный номер {tmp[0]} прошел отсечку {tmp[1]} в {tmp[2][:-2]}"
        if tmp[3][:2] == '00':
            print(printing_data)
            with open(log_file, 'a', encoding="utf-8") as f:
                f.write(f"{datetime.now()} Insert data: {received_data} / Result data: {printing_data}\n")
        else:
            with open(log_file, 'a', encoding="utf-8") as f:
                f.write(f"{datetime.now()} Insert data: {received_data} / Result data: {printing_data}\n")
        client_socket.shutdown(socket.SHUT_RDWR)
        client_socket.close()
except KeyboardInterrupt:
    server.shutdown(socket.SHUT_RDWR)
    server.close()
