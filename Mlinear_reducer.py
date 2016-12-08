#! usr/bin/env python

import sys
import numpy as np 

ind = 0
row_1 = row_2 = row_3 = row_4 = 5*[0] 
for line in sys.stdin:
	line = line.strip().split('\t')
	line = map(lambda x: float(x), line)
	if (ind == 0):
		row_1 = list(map(lambda x: x[0]+x[1], zip(row_1,line)))
	elif (ind == 1):
		row_2 = list(map(lambda x: x[0]+x[1], zip(row_2,line)))
	elif (ind == 2):
		row_3 = list(map(lambda x: x[0]+x[1], zip(row_3,line)))
	elif (ind == 3):
		row_4 = list(map(lambda x: x[0]+x[1], zip(row_4,line))) 
	
	ind += 1
	if (ind == 4):
		ind = 0

arr_XX = np.array([row_1[0:4],row_2[0:4],row_3[0:4],row_4[0:4]])
arr_Xy = np.array([row_1[4] ,row_2[4], row_3[4], row_4[4]])

print(np.matrix(arr_XX))
print(arr_Xy)

arr_XX_I = np.matrix(arr_XX).I

coef_result = arr_XX_I.dot(arr_Xy)
print(coef_result)
