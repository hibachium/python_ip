import ipaddress
import subprocess

import netifaces

eth0_if = netifaces.ifaddresses("eth0")[netifaces.AF_LINK]
eth0_ip = netifaces.ifaddresses("eth0")[netifaces.AF_INET]

mac = eth0_if[0].get("addr")
ipv4 = eth0_ip[0].get("addr")
netmask = eth0_ip[0].get("netmask")
# print(mac)
# print(ipv4)
# print(netmask)
ip = ipaddress.IPv4Network(ipv4 + "/" + netmask, strict=False)
# print(ip)
segment = []

from ping3 import ping, verbose_ping

print(ping("8.8.8.8"))

# for addr in ipaddress.IPv4Network(ip, strict=False):
#     str_addr = str(addr)
#     segment.append(str_addr)
#     subprocess.run(["ping", str_addr, "-c 1", "-t 1", "-i 0.5"])
