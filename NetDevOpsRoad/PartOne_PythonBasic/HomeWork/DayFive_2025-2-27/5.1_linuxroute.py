import os
import re

route_n_result = os.popen("route -n").read()

# print("\n")
# print('>ifconfig_result'+'-'*32)
# print(route_n_result)

gateway = re.findall(r'(\d{1,3}(?:\.\d{1,3}){3})\s+\S+\s+UG', route_n_result)[0]

print(f'网关为: {gateway}')