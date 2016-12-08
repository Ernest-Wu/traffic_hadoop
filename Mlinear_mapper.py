#! usr/bin/env python

import sys
import numpy as np 

index = 0
X_train = []
y_train = []
for line in sys.stdin:
	if (index != 0):
		line = line.strip().split(',')
		x = [float(line[21]), float(line[24]), float(line[25]), float(line[26])]
		y = float(line[28])
		X_train.append(x)
		y_train.append(y)
	index += 1

X_train = np.array(X_train)
y_train = np.array(y_train)

XX = np.dot(X_train.T, X_train)
Xy = np.dot(X_train.T, y_train)

#Inv_XX = np.matrix(XX).I

result = []
ind = 0
for xx,xy in zip(XX, Xy):
	#xx_array = np.array(xx)[0]
	#xx_array_ = '\t'.join(str(x) x in xx_array)
	xx_ = '\t'.join(str(x) for x in xx)
	xx_xy = '\t'.join(str(x) for x in [ind,xx_, xy])
	print(xx_xy)
	

#print(result)
#print(zip(np.array(result)))

