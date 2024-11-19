from ipaddress import ip_address
import socket

host = input ("web name domain : ")
ip_address = socket.gethostbyname(host)

print(f"name domain : {host}")
print(f"IP address : {ip_address}")
