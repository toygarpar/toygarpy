import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET - IP4 formatında bir sabiti tanımlıyoruz, SOCK_STREAM - TCP Protocol

#HOST = "127.0.0.1"
HOST = socket.gethostbyname( socket.gethostname() )
print(HOST)
PORT = 12345

server_socket.bind((HOST,PORT))
server_socket.listen()



while True:
    client_socket, client_address = server_socket.accept() #bağlantı kabul etmek için 


    print(f"Bağlantı yapıldı: {client_address}")

    

    print(client_socket, client_address)


    client_socket.send("Hello".encode("utf-8"))


    server_socket.close()



    break
