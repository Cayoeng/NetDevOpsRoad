from ping import ping_subnet
from ssh import qytang_ssh

import re
import pprint

def qytang_get_if(*ips, username='admin', password='Cisc0123'):
    device_if_dict = {}
    for ip in ips:
       interface_info = qytang_ssh(ip, username, password, cmd='show ip int brief')
       print(interface_info)
       print('='*32)
        # for conn in asa_conn.split('\n '):
        #     re_result = re.match(
        #         r'TCP \S+ (\d{1,3}(?:\.\d{1,3}){3}):(\d{1,5}) \S+ (\d{1,3}(?:\.\d{1,3}){3}):(\d{1,5}), idle \d+:\d+:\d+, bytes (\d+), flags (\S+)',
        #         conn).groups()
        #     asa_dict[re_result[0], re_result[1], re_result[2], re_result[3]] = (re_result[4], re_result[5])

    device_if_dict[ip] = interface_info

    return device_if_dict


subnet = input('Please SUBNET you want to ping: ')

hosts = ping_subnet(subnet)

print(f'\nThere are {len(hosts)} available hosts in subnet {subnet}: \n{hosts}')
print('Now try to get interface information of all hosts except gateway: ')
pprint.pprint(qytang_get_if(*hosts))
