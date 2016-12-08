#! usr/bin/env python

import sys
sys.path.append("/home/lifeng/ruc_wuzhijing")
import numpy as np
import sklearn.datasets
import sklearn.linear_model

def linear_model_coef(X_para, y_para):
	regr = sklearn.linear_model.LinearRegression()
	regr.fit(X_para, y_para)
	return regr.coef_

X_para = []
y_para = []
index = 0
for line in sys.stdin:
	if index !=0:
		line = line.strip().split(',')
		x = [float(line[21]), float(line[24]), float(line[25]),float(line[26])]
		y = float(line[28])
		X_para.append(x)
		y_para.append(y)
	index += 1
y_para = np.array(y_para)
X_para = np.array(X_para)

#print(X_para.shape)
#print(y_para.shape)
model_coef_ = linear_model_coef(X_para, y_para)
ind = 0
for coef in model_coef_:
	print('\t'.join(str(x) for x in [ind, coef]))
	ind += 1

