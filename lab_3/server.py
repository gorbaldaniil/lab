import socket

print("Server IP : " + socket.gethostbyname(socket.gethostname()))
host = socket.gethostbyname(socket.gethostname())
port = 4040

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
i = 0
quit = False
print("[ Server Started ]")

while not quit:
    try:
        data, addr = s.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)


        print("[" + addr[0] + "]=[" + str(addr[1]) + "]/", end="")

        print(data.decode("utf-8"))
        i += 1
        if i == 5:
            print("спіздив лабу, Бодник топ!")
        for client in clients:
            if addr != client:
                s.sendto(data, client)
    except:
        print("\n[ Server Stopped ]")
        quit = True

s.close()
