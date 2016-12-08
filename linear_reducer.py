import sys
import numpy as np

coef_1 = []
coef_2 = []
coef_3 = []
coef_4 = []
for line in sys.stdin:
	line = line.strip().split('\t')
	if (int(line[0]) == 0):
		coef_1.append(float(line[1]))
	elif (int(line[0]) == 1):
		coef_2.append(float(line[1]))
	elif (int(line[0]) == 2):
		coef_3.append(float(line[1]))
	elif (int(line[0]) == 3):
		coef_4.append(float(line[1]))

coef_list = [coef_1, coef_2, coef_3, coef_4]
coef_result = []
for item in coef_list:
	coef_result.append(np.mean(item))

print(coef_result)
