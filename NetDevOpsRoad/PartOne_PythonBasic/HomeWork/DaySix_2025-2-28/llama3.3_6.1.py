
from parse_asa_conn import parse_asa_connections
from print_asa_conn import print_asa_connections

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"
asa_dict = parse_asa_connections(asa_conn)
print_asa_connections(asa_dict)