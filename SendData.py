import socket
IP = input("ip to send data: ")
PORT = input("ip's port to send data: ")
data = b(input("data to send: "))
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(data,(IP,PORT))
