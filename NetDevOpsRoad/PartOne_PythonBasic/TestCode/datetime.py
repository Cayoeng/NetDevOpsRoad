# import datetime
# from datetime import timedelta

# now = datetime.datetime.now()
#
# new_style = now.strftime("%Y-%m-%d %H:%M:%S")
# print(new_style)
#
# ten_days_before = now - timedelta(days=100)
# print(ten_days_before.strftime("%Y-%m-%d %H:%M:%S"))
#
# print(ten_days_before.year)
#
#
# str_time = '2025-02-27 14:20:28'
#
# dt_time = datetime.datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
# print(dt_time)
#
# ten_days_before1 = dt_time - timedelta(days=10)
#
# #print(ten_days_before1)
# ten_days_before1_str = ten_days_before1.strftime('%Y-%m-%d %H:%M:%S')
# print(type(ten_days_before1_str))

import datetime
from dateutil import parser

now = datetime.datetime.now()

gmt_8 = datetime.timezone(datetime.timedelta(hours=8))

print(now.astimezone(gmt_8))