import ipaddress

subnet1 = ipaddress.ip_network('192.168.64.0/24')

hosts = list(subnet1.hosts())

print(hosts)