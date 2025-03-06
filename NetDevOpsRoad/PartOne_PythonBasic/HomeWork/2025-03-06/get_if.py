from ping import ping_subnet
from ssh import qytang_ssh

import re
import pprint

def qytang_get_if(*ips, username='admin', password='Cisc0123'):
    device_if_dict = {}
    for ip in ips:
        if ip == '.'.join(ip.split('.')[0:3]) + '.1':
            continue
        interface_info = qytang_ssh(ip, username, password, cmd='show ip int brief')
        # print(interface_info)
        # print('='*32)

        if_dict = {}

        for str in interface_info.split('\n'):
            re_result = re.match(r'(GigabitEthernet\d+)\s+(\d{1,3}(?:\.\d{1,3}){3})',str)
            if re_result:
                if_dict[re_result.group(1)] = re_result.group(2)

            device_if_dict[ip] = if_dict

    return device_if_dict


subnet = input('Please input SUBNET you want to ping: ')

hosts = ping_subnet(subnet)

print(f'\nThere are {len(hosts)} available hosts in subnet {subnet}: \n{hosts}\n')
print('Now try to get interface information of all hosts except gateway: ')
pprint.pprint(qytang_get_if(*hosts),indent=4)
