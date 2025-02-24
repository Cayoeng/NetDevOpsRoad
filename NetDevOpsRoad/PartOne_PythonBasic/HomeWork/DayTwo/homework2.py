import re

str1 = 'Port-channel1.189   192.168.189.254   YES CONFIG   up   up'

re_result = re.match('([A-Z]\S+\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+YES CONFIG\s+(\w+)\s+\w+', str1).groups()

print(re_result)
print('-'*46)
print(f'{"Interface Name":<20}: {re_result[0]:<20}\n'
      f'{"IP Address":<20}: {re_result[1]:<20}\n'
      f'{"Status":<20}: {re_result[2]:<20}'
      )