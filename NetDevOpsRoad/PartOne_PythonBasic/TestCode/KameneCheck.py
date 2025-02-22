from kamene.all import *
from kamene.layers.inet import IP, ICMP

ping_one_reply = sr1(IP(dst="192.168.109.101")/ICMP(), timeout=1, verbose=False)
ping_one_reply.show()
