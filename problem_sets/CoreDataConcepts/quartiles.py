'''
Adam Forestier
April 28, 2023
'''

import numpy as np

'''
problem statment: print return the IQR from following array:
'''

data = [10, 12, 15, 18, 20, 21, 22, 24, 25, 27, 28, 30, 32, 35, 38, 40, 42, 45, 50]

q1 = np.quantile(a=data, q=.25)
q3 = np.quantile(a=data, q=.75)
iqr = q3 - q1
print(f'First Quartile: {q1}')
print(f'Third Quartile: {q3}')
print(f'IQR: {iqr}')
print(np.quantile(a=data, q=.75))
print(len(data))