import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)

import kamene.layers.inet
from kamene.all import *
from kamene.layers.inet import IP, ICMP

def qytang_ping(ip):
    ping_pkt = kamene.layers.inet.IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return ping_pkt.show()
    else:
        return False

if __name__ == "__main__":
    icmp_dst = input("Please input your ICMP destination IP: ")
    result = qytang_ping(icmp_dst)
    if result:
        print(f'{icmp_dst} 通！')
    else:
        print(f'{icmp_dst} 不通！')