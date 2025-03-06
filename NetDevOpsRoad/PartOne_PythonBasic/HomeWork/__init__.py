import re

ip_address = "192.168.1.1"

a = ip_address.split(".")

new_ip = '.'.join(a[::-2]) + "." + '1'

print(new_ip)