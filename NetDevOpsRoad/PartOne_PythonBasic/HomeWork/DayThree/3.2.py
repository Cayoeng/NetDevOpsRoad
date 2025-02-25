import re

firewall_session_pattern = re.compile(r'(\S+)\s+'                                           #protocol
                                      r'server\s(\d[1,3]+\.\d[1,3]+\.\d[1-3]+\.\d[1,3]+\:\d[1,5]+)\s'    #server
                                      r'localserver\s(\d[1,3]+\.\d[1,3]+\.\d[1-3]+\.\d[1,3]+\d+\:\d[1,5]+)\s'    #localserver
                                      r'idle\s(\d+\:\d+\:\d+)\s'                               #idle
                                      r'bytes\s(\d+)'               #bytes
                                      r'flag\s\S+')              #flags
str = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

re_result = re.match(firewall_session_pattern, str).groups()
print(str)
print('-'*len(str))
print(re_result)
print('-'*len(str))
print(f'{"protocol":<16}: {re_result[0]:<24}\n'
      f'{"server":<16}: {re_result[1]:<24}\n'
      f'{"localserver":<16}: {re_result[2]:<24}\n'
      f'{"idle":<16}: {re_result[3]:<24}\n'
      f'{"bytes":<16}: {re_result[4]:<24}\n'
      f'{"flags":<16}: {re_result[5]:<24}'
      )