from ping import ping_subnet
from ssh import qytang_ssh

import re
import pprint

def qytang_get_if(*ips, username='admin', password='Cisc0123'):
    device_if_dict = {}
    for ip in ips:
        device_if_dict[ip] = qytang_ssh(ip, username, password, cmd='show ip int brief')
    return device_if_dict


subnet = input('Please SUBNET you want to ping: ')

hosts = ping_subnet(subnet)

print(f'\nThere are {len(hosts)} available hosts in subnet {subnet}: \n{hosts}')
print('Now try to get interface information of all hosts except gateway: ')
pprint.pprint(qytang_get_if(*hosts))
