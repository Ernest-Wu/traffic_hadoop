#! usr/bin/env python

import sys
import datetime

def f(x):
	year = x[0]
	month = x[1]
	day = x[2]
	hour = x[3]
	minute = x[4]
	if hour == 99:
		hour = 0
	if minute == 99:
		minute = 0
	s = "%02d-%02d-%02d %02d:%02d:00" % (year,month,day,hour,minute)
	c = datetime.datetime.strptime(s,'%Y-%m-%d %H:%M:%S')
	return c

MONTH_count = {}
index = 0
for line in sys.stdin:
	if index != 0:
		line = line.strip().split(',')
		item1,item2,item3,item4,item5 = int(line[13]),int(line[12]),int(line[11]),int(line[15]),int(line[16])
		TIME_item = [item1,item2,item3,item4,item5]
		crashTime = f(TIME_item)
		crashMonth = crashTime.strftime("%B")
		if crashMonth not in MONTH_count:
			MONTH_count[crashMonth] = 1
		else:
			MONTH_count[crashMonth] += 1
	index += 1

for month, count in MONTH_count.items():
	print(': '.join([str(x) for x in [month, count]]))


