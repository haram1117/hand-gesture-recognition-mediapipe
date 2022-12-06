import socket
import time
from datetime import datetime

def SocketSetup():
    # global HOST
    HOST = '192.168.35.243' 
    # global PORT
    PORT = 8000
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    global client_socket, addr
    client_socket, addr = server_socket.accept()
    print('Connected by', addr)


def SendHandPosition(x, y):
    msg = f'x: {x}, y: {y}'
    client_socket.sendall(msg.encode())
    print('send 완료: ' + msg)
    time.sleep(0.01)

def SendIsClosed(isClosed):
    msg = f'isClosed: {isClosed}'
    client_socket.sendall(msg.encode())
    print('send 완료: ' + msg)
    # time.sleep(0.01)


def closeSocket():
    client_socket.close()
    server_socket.close()
