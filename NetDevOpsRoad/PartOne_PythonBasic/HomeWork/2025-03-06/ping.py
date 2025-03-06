import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)

import kamene.layers.inet
from kamene.all import *
from kamene.layers.inet import IP, ICMP

import ipaddress
from concurrent.futures import ThreadPoolExecutor, as_completed


def qytang_ping(ip):
    # 单个IP的Ping测试，成功返回True，失败返回False
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=1, verbose=False)
    return True if ping_result and ping_result.type == 0 else False


def multi_ping_ips(ips,max_workers=8):
    """
    对给定的一批IP地址使用多线程并发Ping，返回 {ip: Bool} 的字典：
        - True 表示 ICMP Reply 收到
        - False 表示 Ping 不通
    """
    results = {}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # future_to_ip 映射每个线程任务到其对应的IP
        future_to_ip = {
            executor.submit(qytang_ping, ip): ip
            for ip in ips
        }
        for future in as_completed(future_to_ip):
            ip = future_to_ip[future]
            try:
                results[ip] = future.result()
            except Exception:
                results[ip] = False
    return results


def ping_subnet(network, max_workers=8):
    """
    对网段 network 中的所有主机地址进行并发Ping，
    返回一个仅包含可达IP的列表
    """
    net = ipaddress.ip_network(network)
    ip_list = [str(ip) for ip in net.hosts()]

    print(ip_list)

    ping_dict = multi_ping_ips(ip_list, max_workers)

    print('-'*50)
    print(ping_dict)

    reachable_hosts = [ip for ip, reachable in ping_dict.items() if reachable]
    return reachable_hosts


if __name__ == "__main__":
    # 示例：多线程批量Ping一组IP
    test_ips = ["192.168.64.101", "8.8.8.8"]
    results = multi_ping_ips(test_ips)
    print("Ping 测试结果：")
    for ip, status in results.items():
        print(f"  {ip}: {status}")

    # 示例：对网段 192.168.64.0/24 进行扫描并返回连通的 IP
    reachable = ping_subnet("192.168.64.0/24")
    print(f"\n子网扫描可达IP: {reachable}")

