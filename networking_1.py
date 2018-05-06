import socket
import sqlmap
socket.setdefaulttimeout(2)

s = socket.socket()

s.connect(("www.screencastify.com",21))

ans = s.recv(1024)

print ans
