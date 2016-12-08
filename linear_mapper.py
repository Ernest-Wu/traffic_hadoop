#! usr/bin/env python

import sys
sys.path.append("/home/lifeng/ruc_wuzhijing")
import numpy as np
import sklearn.datasets
import sklearn.linear_model

def linear_model_coef(X_para, y_para):
	regr = linear_model.LinearRegression()
	regr.fit(X_para, y_para)
	return regr.coaf_

X_para = np.array([])
y_para = []
index = 0
for line in sys.stdin:
	if index !=0:
		line = line.strip().split(',')
		x = np.array([float(line(21)), float(line(24)), float(line(25)),float(line(26))])
		y = float(line(28))
		X_para = np.concatenate((X_para, x))
		y_para.append(y)
	index += 1
y_para = np.array(y_para)

print(linear_model_coef(X_para, y_para))


