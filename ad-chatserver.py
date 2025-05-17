import socket



PORT = 12345
SERVER =  socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"
BYTESIZE = 1024
DISCONNECT_MSG = "quit"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)


server.listen()
print("server çalışıyor...\n")


client_socket, client_address =  server.accept()

client_socket.send("Sunucu bağlantınız yapıldı.\n".encode(FORMAT))




while True:
    msg = client_socket.recv(BYTESIZE).decode(FORMAT)

    if msg == DISCONNECT_MSG:
        client_socket.send("quit".encode(FORMAT))
        print("çıkış yapıldı")
        break
    else:
        print(f"{msg}\n")
        msg = input("Mesaj yaz: ")
        client_socket.send(msg.encode(FORMAT))


client_socket.close()
