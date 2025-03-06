import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)

import kamene.layers.inet
from kamene.all import *
from kamene.layers.inet import IP, ICMP

import ipaddress

def qytang_ping(ip):
    ping_pkt = kamene.layers.inet.IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return True
    else:
        return False


def ping_subnet(network):
    # 使用ipaddress模块解析子网
    net = ipaddress.ip_network(network)
    reachable_hosts = []
    # 对子网内所有主机地址循环测试
    for ip in net.hosts():
        # 调用已有qytang_ping函数构建ICMP报文
        if qytang_ping(str(ip)):
            reachable_hosts.append(str(ip))
    return reachable_hosts