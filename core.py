import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

vals_total = 1000
vals = np.random.normal(0,1,vals_total)
seq = np.cumsum(vals)
colname = 'simulated'
data = pd.DataFrame(data = seq, index = range(vals_total), columns = [colname])


regression_out = 50

'''
entry_points = 20
entries = np.random.choice(range(vals_total-regression_out), entry_points)

for entry in entries:
    d = data[colname][entry:entry + regression_out].values.reshape(-1,1)
    r = np.array ( [i for i in range(regression_out)] ).reshape(-1, 1)
    reg = LinearRegression().fit(r, d)
    res = reg.predict(r)

    data[str(entry) + '_' + str(round(reg.coef_[-1][-1], 4))] = pd.Series (data = res.reshape(-1), index = range(entry, entry+regression_out))
    
'''
coef = []

for i in range(vals_total-regression_out):

    v = data[colname] [i:i+regression_out].values.reshape(-1,1)
    r = np.array ( [i for i in range(regression_out)] ).reshape(-1, 1)
    print (v, r)
    reg = LinearRegression().fit(r, v)
    coef.append(reg.coef_)


data['coeff'] = pd.Series(data = np.array(coef).reshape(-1), index = range(vals_total-regression_out))

data['bins'] = pd.qcut(data['coeff'].dropna(), q = 20)
#print (data)
bins  = data['bins'].value_counts().index.values

for b in bins:

    data['binned_' + str(b)] = data['simulated'] [data['bins'] == b]


st.plot