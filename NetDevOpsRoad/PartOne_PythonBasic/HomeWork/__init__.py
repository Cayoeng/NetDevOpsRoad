import re

ip_address = "192.168.1.1"

a = ip_address.split(".")

print(a)

new_ip = '.'.join(a[0:3]) + "." + '1'

print(new_ip)