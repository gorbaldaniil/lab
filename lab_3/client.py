import socket, threading, time

def caesars(text, key):
    i = -1
    result = ""

    for num in text.split():
        i += 1
        if num.isdigit():
            num = str(int(num) + key)
            inputWords = text.split()
            inputWords[i] = num
            result += ''.join(num)
            try:
                test = text.split()[i + 1]
                result += " "
            except:
                pass
            continue

        for letters in num:
            ordValue = ord(letters)
            cipherValue = ordValue + key
            if cipherValue == ord(" ") + key:
                cipherValue -= key
            elif cipherValue > ord("0") and cipherValue <= ord(":"):
                cipherValue = ordValue + key

            elif 65 <= ordValue <= 90:
                cipherValue = (ordValue - 65 + key) % 26 + 65
            elif 97 <= ordValue <= 122:
                cipherValue = (ordValue - 97 + key) % 26 + 97  # eng

            elif 1072 <= ordValue <= 1103:
                cipherValue = (ordValue - 1072 + key) % 32 + 1072

            elif 1040 <= ordValue <= 1071:
                cipherValue = (ordValue - 1071 + key) % 32 + 1071

            result += chr(cipherValue)

        try:
            test = text.split()[i + 1]
            result += " "
        except:
            pass

    return result

key = 1
shutdown = False
join = False


def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)

                decrypt = "";
                k = False
                for i in data.decode("utf-8"):
                    if i == ":":
                        k = True
                        decrypt += i
                    elif k == False or i == " ":
                        decrypt += i
                    else:
                        decrypt += caesars(i, -key)
                print(decrypt)
                # End

                time.sleep(0.2)
        except:
            pass


host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("192.168.0.103", 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

alias = input("Name: ")

rT = threading.Thread(target=receving, args=("RecvThread", s))
rT.start()

while shutdown == False:
    if join == False:
        s.sendto(("[" + alias + "] => join chat ").encode("utf-8"), server)
        join = True
    else:
        try:
            message = input()

            message = caesars(message, 1)

            if message != "":
                s.sendto(("[" + alias + "] :: " + message).encode("utf-8"), server)

            time.sleep(0.2)
        except:
            s.sendto(("[" + alias + "] <= left chat ").encode("utf-8"), server)
            shutdown = True

rT.join()
s.close()
