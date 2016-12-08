import numpy as np 
import pandas as pd 
import datetime

import warnings
import matplotlib.pyplot as plt 
import seaborn as sns
sns.set_style('whitegrid')
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools
from plotly.offline import iplot

from subprocess import check_output

#print(check_output(["ls", "/Users/ErnestWu/Desktop/python/traffic/2015-traffic-fatalities"]).decode("utf8"))

# Read data accident.csv
FILE="/Users/ErnestWu/Desktop/python/traffic/2015-traffic-fatalities/accident.csv"
d=pd.read_csv(FILE)
#print(d.head(5))

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
	
d['crashTime']   = d[['YEAR','MONTH','DAY','HOUR','MINUTE']].apply(f, axis=1)
#print(d['crashTime'].apply(lambda x: x.date()).head(5))
d['crashDay']    = d['crashTime'].apply(lambda x: x.date())
d['crashMonth']  = d['crashTime'].apply(lambda x: x.strftime("%B"))
d['crashMonthN'] = d['crashTime'].apply(lambda x: x.strftime("%d"))
#print(d[['crashMonth', 'crashMonthN']].head(5))
month_cnt = {}
for item in d['crashMonth']:
	if item not in month_cnt:
		month_cnt[item] = 1
	else:
		month_cnt[item] += 1
#print(month_cnt)
for month,count in month_cnt.items():
	print(month+': '+str(count))
#print(d['crashMonth'])
print(d[[1,2]].head(5))

