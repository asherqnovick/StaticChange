import psutil

interfaces = psutil.net_if_addrs()
for interface, info in interfaces.items():
	address = info[1].address
	netmask = info[1].netmask
	print(interface, address, netmask)	

