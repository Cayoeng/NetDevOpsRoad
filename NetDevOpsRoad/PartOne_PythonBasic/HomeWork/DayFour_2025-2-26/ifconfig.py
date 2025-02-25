import os
import re

ifconfig_result = os.popen("ifconfig " + "eth0").read()

print("\n")
print('>ifconfig_result'+'-'*32)
print(ifconfig_result)


#正则表达式查找ip，mask，broadcast和mac
ipv4_add = re.findall(r'inet (\d{1,3}(?:\.\d{1,3}){3})', ifconfig_result)[0]
netmask = re.findall(r'netmask (\d{1,3}(?:\.\d{1,3}){3})', ifconfig_result)[0]
broadcast = re.findall(r'broadcast (\d{1,3}(?:\.\d{1,3}){3})', ifconfig_result)[0]
mac = re.findall(r'ether (([0-9A-Fa-f]{2}[-:]){5}[0-9A-Fa-f]{2})', ifconfig_result)[0][0]

#格式化字符串
format_string = '{0:<20}: {1:<20}'

#打印结果
print('>format_result'+'-'*32)
print(format_string.format('ipv4_add', ipv4_add))
print(format_string.format('netmask', netmask))
print(format_string.format('broadcast', broadcast))
print(format_string.format('mac', mac))

#产生网关的IP地址
ipv4_add_list = ipv4_add.split('.')
ipv4_gw = ipv4_add_list[0] + '.' + ipv4_add_list[1] + '.' + ipv4_add_list[2] + '.1'

#打印网关的IP地址
print('\n>ping_result'+'-'*32)
print('我们假设网关IP地址最后一位是1，因此网关IP地址为：' + ipv4_gw + '\n')

#Ping网关
ping_result = os.popen("ping " + ipv4_gw + ' -c 1').read()
print(ping_result)


re_ping_result = re.findall(r'0% packet loss,', ping_result)[0]

if re_ping_result:
    print('网关可达！')
else:
    print('网关不可达！')