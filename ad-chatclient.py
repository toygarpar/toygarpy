import socket



PORT = 12345
SERVER =  socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"
BYTESIZE = 1024
DISCONNECT_MSG = "quit"



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)


while True:
    msg = client.recv(BYTESIZE).decode(FORMAT)

    if msg == DISCONNECT_MSG:
        client.sen("quit".encode(FORMAT))
        #client.send("Çıkış Yapıldı".encode(FORMAT))
        print("çıkış yapılıyor...")
        break
    else:
        print(f"{msg}\n")
        msg = input("Mesaj yaz: ")
        client.send(msg.encode(FORMAT))


client.close()