import sys

STATE_count = {}
for line in sys.stdin:
	line = line.strip.split('\t')
	if line[0] not in STATE_count:
		STATE_count[line[0]] = 0
	else:
		STATE_count[line[0]] += 1

for state, count in STATE_count.items():
	print('\t'.join([str(x) for x in [state, count]]))

# 	STATE_set.append(line[0])
# N = len(STATE_set)

# for i in range(1,8):
# 	if (N - i*BINWIDTH) < 0:
# 		break
# 	else:
# 		STATE_bin.append((i, STATE_set[(i-1)*BINWIDTH:i*BINWIDTH]))
# 	i = 0



# import numpy as np 
# import pandas as pd 
# import datetime

# #FILE = "/home/lifeng/ruc_wuzhijing/homework1/2015-traffic-fatalities"
# dat=pd.read_csv(accident.csv)

# def f(x):
# 	year = x[0]
# 	month = x[1]
# 	day = x[2]
# 	hour = x[3]
# 	minute = x[4]
# 	if hour == 99:
# 		hour = 0
# 	if minute == 99:
# 		minute = 0
# 	s = "%02d-%02d-%02d %02d:%02d:00" % (year,month,day,hour,minute)
# 	c = datetime.datetime.strptime(s,'%Y-%m-%d %H:%M:%S')
# 	return c
# dat['crashTime']   = dat[['YEAR','MONTH','DAY','HOUR','MINUTE']].apply(f, axis=1)
# #print(d['crashTime'].apply(lambda x: x.date()).head(5))
# dat['crashDay']    = dat['crashTime'].apply(lambda x: x.date())
# dat['crashMonth']  = dat['crashTime'].apply(lambda x: x.strftime("%B"))
# dat['crashMonthN'] = dat['crashTime'].apply(lambda x: x.strftime("%d"))

# print(dat['crashMonth'])