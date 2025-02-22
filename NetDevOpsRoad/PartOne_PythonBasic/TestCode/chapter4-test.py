# str1 = 'Welcome to Beijing'
# list_str = list(str1)
# print(list_str)
#
# print('-'*90)
#
# list_str[8] = 'T'
# print(list_str)
#
# print('-'*90)
# print(''.join(list_str))

#x = 1234
# #直接打印，左对齐宽度10，右对齐宽度10，左补零宽度10
# res = 'integers:...+%d<...+%-10d<...+%10d<...+%010d<' % (x, x, x, x)
# print(res)
# #输出：integers:...+1234<...+1234      <...+      1234<...+0000001234<

# x = 1.23456789
# #加号就表示普通加号，6表示%右边的整体宽度
# #左对齐、宽度6、小数点后两位、浮点数
# #左补零、宽度5、小数点后两位、浮点数
# #左补零、%右边宽度6、小数点后一位、浮点数
# #左补零、%右边宽度6、小数点后一位、浮点数
# res = '%-6.2f|%05.2f|%+06.1f|+%06.1f' % (x, x, x, x)
# print(res)

# #字符串格式化表达式高级示例-字典键测试
# qytdict = {'test': 12345.1234}
# #左对齐、宽度20、小数点后两位、浮点数
# res = 'test:%(test)-20.2f' % qytdict
# print(res)

# str_format = '{}, {} and {}'
# print(str_format.format('Hello', 'World', 'Python'))
# print('-'*24)
# str_format1 = '{1}, {0} and {2}'
# print(str_format1.format('Hello', 'World', 'Python'))

# import sys
# str_format3 = '{0.platform:>10}={1[kind]:<10}'.format(sys, dict(kind='workstation'))
# print(str_format3)

# import sys
# system_info = {'platform': sys.platform, 'kind': 'workstation'}
# str_format3 = '{0[platform]:>10}={0[kind]:<10}'.format(system_info)
# print(str_format3)

# import sys
# system_info = {'platform': sys.platform, 'kind': 'workstation'}
# str_format3 = f'{system_info["platform"]:>10}={system_info["kind"]:<10}'
# print(str_format3)

# #格式化字符串f-string
# str_format4 = f'{123456789.123456789:>10.2f}'
# print(str_format4)

# # 基础数值格式化
# number = 1234.5678
# price = 99.9
# name = "Python"
#
# # 1. 数值格式化
# print(f"整数补零: {number:08.2f}")  # 输出: 01234.57
# print(f"金额表示: {price:>10.2f}元")  # 输出: "     99.90元"
# print(f"百分比: {0.15:.1%}")  # 输出: "15.0%"
#
# # 2. 字符串对齐
# print(f"|{name:^15}|")  # 居中对齐，输出: "|     Python    |"
# print(f"|{name:>15}|")  # 右对齐，输出:  "|         Python|"
# print(f"|{name:<15}|")  # 左对齐，输出:  "|Python         |"
#
# # 3. 字典格式化
# person = {'name': 'Alice', 'age': 25}
# print(f"姓名: {person['name']:<10} 年龄: {person['age']:03d}岁")  # 输出: "姓名: Alice      年龄: 025岁"
#
# # 4. 表达式计算
# x = 10
# # y = 20
# # print(f"计算结果: {x} + {y} = {x + y}")  # 输出: "计算结果: 10 + 20 = 30"
# #
# # # 5. 日期时间格式化
# # from datetime import datetime
# #
# # now = datetime.now()
# # print(f"当前时间: {now:%Y-%m-%d %H:%M:%S}")  # 输出: "当前时间: 2024-03-14 15:30:45"
# #
# # # 6. 科学计数法
# # big_number = 1234567.89
# # print(f"科学计数: {big_number:e}")  # 输出: "科学计数: 1.234568e+06"
# # print(f"精确控制: {big_number:.2e}")  # 输出: "精确控制: 1.23e+06"
# #
# # # 7. 进制转换
# # number = 255
# # print(f"十进制: {number:d}")  # 输出: "十进制: 255"
# # print(f"十六进制: {number:#x}")  # 输出: "十六进制: 0xff"
# # print(f"八进制: {number:#o}")  # 输出: "八进制: 0o377"
# # print(f"二进制: {number:#b}")  # 输出: "二进制: 0b11111111"
#
#
#
import re
showIpArp = """
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.1.2.1                -   000c.2908.3b71  ARPA   GigabitEthernet2
Internet  192.168.109.101         -   000c.2908.3b67  ARPA   GigabitEthernet1
Internet  192.168.109.102        71   000c.2991.b75b  ARPA   GigabitEthernet1
Internet  192.168.109.129         0   000c.2900.9051  ARPA   GigabitEthernet1
"""
#
# ARP_TABLE1 = [
#     {
#         "Protocol": "Internet",
#         "Address": "10.1.2.1",
#         "Age (min)": "-",
#         "Hardware Addr": "000c.2908.3b71",
#         "Type": "ARPA",
#         "Interface": "GigabitEthernet2"
#     },
#     {
#         "Protocol": "Internet",
#         "Address": "192.168.109.101",
#         "Age (min)": "-",
#         "Hardware Addr": "000c.2908.3b67",
#         "Type": "ARPA",
#         "Interface": "GigabitEthernet1"
#     },
#     {
#         "Protocol": "Internet",
#         "Address": "192.168.109.102",
#         "Age (min)": "71",
#         "Hardware Addr": "000c.2991.b75b",
#         "Type": "ARPA",
#         "Interface": "GigabitEthernet1"
#     },
#     {
#         "Protocol": "Internet",
#         "Address": "192.168.109.129",
#         "Age (min)": "0",
#         "Hardware Addr": "000c.2900.9051",
#         "Type": "ARPA",
#         "Interface": "GigabitEthernet1"
#     }
# ]
#
# print(ARP_TABLE1)
# print("-"*100)
# print("The Hardware Addr of all devices:")
# #第一种：遍历列表，找出所有配合关键字“Hardware Addr”的值
# #for hardware_addr in ARP_TABLE1:
# #    print(hardware_addr.get("Hardware Addr"))
#
# #第二种：
# for entry in ARP_TABLE1:
#     print(f'Hardware Addr: {entry["Hardware Addr"]:<10s}')

print(showIpArp)
print("-"*100)
sTring1 = showIpArp.splitlines()
print(sTring1)
print("-"*100)
print(sTring1[5].split())
print("-"*100)
print(sTring1[5].split()[1])


print(showIpArp.splitlines()[5].split()[1])
