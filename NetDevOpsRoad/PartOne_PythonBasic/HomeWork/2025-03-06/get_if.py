from ping import ping_subnet
from ssh import qytang_ssh

import re
import pprint

def qytang_get_if(*ips, username='admin', password='Cisc0123'):
    device_if_dict = {}
    for ip in ips:
        if ip != '192.168.64.1':
            continue
        interface_info = qytang_ssh(ip, username, password, cmd='show ip int brief')
        # print(interface_info)
        # print('='*32)

        if_dict = {}
        for str in interface_info.split('\n'):
            re_result = re.match(r'(GigabitEthernet\d+)\s+(\d{1,3}(?:\.\d{1,3}){3})',str).groups()
            if_dict[re_result[0]] = re_result[1]

        device_if_dict[ip] = if_dict

    return device_if_dict


subnet = input('Please SUBNET you want to ping: ')

hosts = ping_subnet(subnet)

print(f'\nThere are {len(hosts)} available hosts in subnet {subnet}: \n{hosts}')
print('Now try to get interface information of all hosts except gateway: ')
pprint.pprint(qytang_get_if(*hosts))
