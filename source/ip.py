from ipaddress import IPv4Network
from socket import gethostbyname, gethostname

import netifaces

ipv4 = gethostbyname(gethostname())
print(ipv4)

segment = IPv4Network(ipv4, strict=True)
print(segment)

ip = netifaces.ifaddresses("eth0")

print(ip)
