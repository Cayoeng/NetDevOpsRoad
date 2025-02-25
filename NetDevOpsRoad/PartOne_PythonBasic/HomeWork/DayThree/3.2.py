import re

#创建pattern，用正则表达式匹配防火墙会话
firewall_session_pattern = re.compile(r'(TCP|UDP)\s+'                                           #protocol
                                      r'server\s+(\d{1,3}(?:\.\d{1,3}){3}:\d{1,5})\s+'          #server
                                      r'localserver\s+(\d{1,3}(?:\.\d{1,3}){3}:\d{1,5}),\s+'    #localserver
                                      r'idle\s+(\d+):(\d+):(\d+),\s'                            #idle hour:minute:second
                                      r'bytes\s+(\d+),\s+'                                      #bytes
                                      r'flags\s+(\S+)')                                         #flags


#操作对象-防火墙会话（范例）
str = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

print('>'*3+'-'*(len(str)-6)+'<'*3)
print(f'The INPUT IS BELLOW:\n{str}\n')
print('>'*3+'-'*(len(str)-6)+'<'*3)


#用自定义pattern匹配字符串，确定匹配成功后，进行groups动作
re_result = re.match(firewall_session_pattern, str)
print(f'The type of re_result is: {type(re_result)}')

if re_result:
    print(f'MATCHED! THE RESULT IS:\n{re_result.groups()}\n')
    print(f'The type of re_result.groups() is: {type(re_result.groups())}\n')
else:
    print('NOT MATCH!')

print('>'*3+'-'*(len(str)-6)+'<'*3)


#格式化打印结果
print(f'THE FINAL RESULT IS:\n'
      f'{"protocol":<16}: {re_result.groups()[0]:<24}\n'
      f'{"server":<16}: {re_result.groups()[1]:<24}\n'
      f'{"localserver":<16}: {re_result.groups()[2]:<24}\n'
      f'{"idle":<16}: {re_result.groups()[3]:<2}小时{re_result.groups()[4]:>2}分钟{re_result.groups()[5]:>2}秒\n'
      f'{"bytes":<16}: {re_result.groups()[6]:<24}\n'
      f'{"flags":<16}: {re_result.groups()[7]:<24}'
      )