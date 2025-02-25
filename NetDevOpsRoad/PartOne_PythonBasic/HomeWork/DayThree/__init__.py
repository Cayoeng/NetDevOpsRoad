import ipaddress

subNet1 = ipaddress.ip_network('192.168.1.0/24')

for ipAddr in subNet1:
    print(f'{ipAddr}/24')
ip1 = ipaddress.ip_address('192.168.1.100')

print('-'*20)
print(f'{ip1} is in {subNet1}: True or False')
print(ip1 in subNet1)
print('-'*20)
print(subNet1)
