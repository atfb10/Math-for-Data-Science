'''
Adam Forestier
May 5, 2023
'''

import numpy as np

# Functions

def covariance(x: list, y: list) -> float:
    if len(x) != len(y):
        raise ValueError('x and y must be the same length')
    
    numerator = 0
    n = len(x) - 1
    x_hat = np.mean(x)
    y_hat = np.mean(y)
    for i in range(0, len(x)):
        numerator += (x[i] - x_hat) * (y[i] - y_hat)
    return round((numerator / n), 2) 

def standard_deviation(data: list) -> float:
    numerator = 0
    n = len(data) - 1
    x_hat = np.mean(data)
    for i in range(0, len(data)):
        numerator += (data[i] - x_hat) ** 2
    variance = round((numerator / n), 2)
    print(np.sqrt(variance))
    return np.sqrt(variance)

def pearson_correlation(x: list, y: list) -> float:
    cov = covariance(x=x, y=y)
    std_x = standard_deviation(data=x)
    std_y = standard_deviation(data=y)
    corr = cov / (std_x * std_y)
    return round(corr, 2)


# Question 1
x = [1.7, 2.4, .1, .5, -2.5, 6.6, 1.5, .2, .1, 2.1, 3.1, -1.1]
y = [-.1, -.3, 3.2, 2.5, 5.2, -1.3, .2, 1.8, 2.2, .3, .1, 1.9]

answer1a = covariance(x, y)
print(answer1a) # -3.67
answer1b = 'Monthly returns between the two stocks are negatively correlated'

# Question 2
answer2 = pearson_correlation(x=x, y=y)
print(answer2)