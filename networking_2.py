import socket
import requests
socket.setdefaulttimeout(2)

s = socket.socket()

s.connect(("www.screencastify.com",21))

ans = s.recv(1024)

if ("FreeFloat Ftp Server (Version 1.00)" in ans):
    print "[+] FreeFloat FTP Server is vulnerable"
elif ("3Com 3CDaemon FTP Server is vulnerable" in banner):
    print "[+] 3CDaemon FTP Server is vulnerable."
elif ("Ability Server 2.34" in banner):
    print "[+] Ability FTP Server is vulnerable."
elif ("Sami FTP Server 2.0.2" in banner):
    print "[+] Sami FTP Server is vulnerable."
else:
    print "[+] FTP Server is not vulnerable."
