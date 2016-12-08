import sys

COUNT_list = []

for line in sys.stdin:
	line = line.strip().split('\t')
	state = line[0]
	count = int(line(1))
	COUNT_list.append((state, count))

COUNT_list = sorted(COUNT_list, key = lambda x: x[1],reverse = True)

for state, count in COUNT_list:
	print('\t'.join([str(x) for x in [state, count]]))

# month_cnt = {}
# for line in sys.stdin:
# 	if line not in month_cnt:
# 		month_cnt[line] = 1
# 	else:
# 		month_cnt[line] += 1

# for month,count in month_cnt.items():
# 	print(month+': '+str(count))