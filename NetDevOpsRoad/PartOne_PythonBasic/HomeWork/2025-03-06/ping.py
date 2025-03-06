import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)

import kamene.layers.inet
from kamene.all import *
from kamene.layers.inet import IP, ICMP

import ipaddress

from concurrent.futures import ThreadPoolExecutor, as_completed


def qytang_ping(ip):
    ping_pkt = kamene.layers.inet.IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=1, verbose=False)

    print(ping_result)

    if ping_result and ping_result.type == 0:
        return True
    else:
        return False

# 单线程
# def ping_subnet(network):
#     # 使用ipaddress模块解析子网
#     net = ipaddress.ip_network(network)
#     reachable_hosts = []
#     # 对子网内所有主机地址循环测试
#     for ip in net.hosts():
#         # 调用已有qytang_ping函数构建ICMP报文
#         if qytang_ping(str(ip)):
#             reachable_hosts.append(str(ip))
#     return reachable_hosts

#多线程
def ping_subnet(network):
    """使用多线程对给定子网的所有主机进行Ping测试，并返回可达的IP列表"""
    net = ipaddress.ip_network(network)

    reachable_ips = []

    with ThreadPoolExecutor(max_workers=8) as executor:
        # 建立一个字典：Future对象对应要Ping的IP
        future_to_ip = {
            executor.submit(qytang_ping, str(ip)): str(ip)
            for ip in net.hosts()
        }

        for future in as_completed(future_to_ip):
            ip = future_to_ip[future]
            try:
                # 如果结果为 True，说明Ping通
                if future.result():
                    reachable_ips.append(ip)
            except Exception as e:
                # 这里可以处理异常日志等
                pass

    return reachable_ips
