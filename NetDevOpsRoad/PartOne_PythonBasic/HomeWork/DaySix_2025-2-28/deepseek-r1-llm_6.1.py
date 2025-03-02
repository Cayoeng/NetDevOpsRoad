import re

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"
asa_dict = {}

for conn in asa_conn.split('\n '):
    re_result = re.match(
        r'TCP \S+ (\d{1,3}(?:\.\d{1,3}){3}):(\d{1,5}) \S+ (\d{1,3}(?:\.\d{1,3}){3}):(\d{1,5}), idle \d+:\d+:\d+, bytes (\d+), flags (\S+)',
        conn).groups()
    asa_dict[re_result[0], re_result[1], re_result[2], re_result[3]] = (re_result[4], re_result[5])

# Improved formatting
print("\nConnection Analysis Results:\n")
format_str = "{:<20} | {:<10} | {:<20} | {:<10} | {:<8} | {}"
header = "Source IP".ljust(20) + " | " + "Port".ljust(10) + " | " + "Destination IP".ljust(20) + " | "+"DST PORT".ljust(10) + " | " + "Bytes".ljust(8) + " | Flags"
print(header)
print('-'*len(header))

for key, value in asa_dict.items():
    src_ip = key[0]
    src_port = key[1]
    dst_ip = key[2]
    dst_port = key[3]
    print(format_str.format(src_ip,src_port,dst_ip,dst_port,value[0],value[1]))