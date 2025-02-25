
import re

firewall_session_pattern = re.compile(r'(TCP|UDP)\s+'                                                               #protocol
                                      r'server\s+(\d{1,3}(?:\.\d{1,3}){3}:\d{1,5})\s+'             #server
                                      r'localserver\s+(\d{1,3}(?:\.\d{1,3}){3}:\d{1,5}),\s+'     #localserver
                                      r'idle\s+(\d+:\d+:\d+),\s'                                                 #idle
                                      r'bytes\s+(\d+),\s+'                                                              #bytes
                                      r'flags\s+(\S+)'
                                      )                                                                #flags

#str = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
str = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

print(str)
print('-'*len(str))

re_result = re.match(firewall_session_pattern, str)
if re_result:
    print(re_result.groups())
else:
    print('Not Match')
print('-'*len(str))