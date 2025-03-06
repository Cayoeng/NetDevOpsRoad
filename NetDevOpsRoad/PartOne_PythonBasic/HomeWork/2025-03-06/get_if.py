from ping import ping_subnet
from ssh import qytang_ssh

subnet = input("Please SUBNET you want to ping: ")

hosts = ping_subnet(subnet)

print(f"There are {len(hosts)} available hosts in subnet {subnet}: ")

print(hosts)

# interface_list = {}
# for host in hosts:
#     qytang_ssh(host, 'admin', 'Cisc0123', cmd='show ip int brief')