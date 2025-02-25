import re

str = '166  54a2.74f7.0326  DYNAMIC  Gi1/0/11'

re_result = re.match('(\d+)\s+(\S+)\s+(\S+)\s+(\S+)', str).groups()
print(re_result)
print('-'*48)
print(f'{"VLAN ID":<10}: {re_result[0]:<10}\n'
      f'{"MAC":<10}: {re_result[1]:<10}\n'
      f'{"Type":<10}: {re_result[2]:<10}\n'
      f'{"Interface":<10}: {re_result[3]:<10}'
      )