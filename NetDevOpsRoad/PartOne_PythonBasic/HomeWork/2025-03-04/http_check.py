import time
import psutil

def check_http_port(port):
    for conn in psutil.net_connections(kind='tcp'):
        if conn.status == 'LISTEN' and conn.laddr.port == port:
            return True

while True:
    if check_http_port(80):
        print("HTTP(TCP/80)服务已经被打开.")
        break
    else:
        print("等待1秒后重新开始监控！")
        time.sleep(3)