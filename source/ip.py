import netifaces

interface = netifaces.ifaddresses("eth0")[netifaces.AF_LINK]
ipaddress = netifaces.ifaddresses("eth0")[netifaces.AF_INET]

mac = interface[0].get("addr")
ipv4 = ipaddress[0].get("addr")
netmask = ipaddress[0].get("netmask")
print(mac)
print(ipv4)
print(netmask)
