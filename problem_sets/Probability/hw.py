'''
Adam Forestier
April 30, 2023
'''

import numpy as np

'''
Question 1:
'''
answer1 = 'No, this is the experimental probability with a small sample size'

'''
Question 2:
'''
# Infinitely
answer_2a = 'infinitely'
answer_2b = '100,000 - the Law of Large Numbers'

'''
Question 3
'''
company1 = {'yield': .99, 'chance': .10}
company2 = {'yield': .10, 'chance': .99}
company3 = {'yield': 10.00, 'chance': .01}
investment = 10000

answer_3a = company1['chance'] * company2['chance'] * company3['chance']
answer_3b = investment * company1['chance'] * company1['yield']
answer_3c = 1 - (company1['chance'] * company2['chance'] * company3['chance'])
answer_3d = company1['chance'] * (1 - company2['chance']) * (1 - company2['chance'])

'''
Question 4
'''
uninfected = 325000000 - 10000
p_of_a = 10000 / 325000000
p_b_conditional_a = .99
infected_and_positive = .99 * p_of_a
not_infected_and_positive = .01 * uninfected
p_of_b = infected_and_positive + not_infected_and_positive

answer_4 = (p_b_conditional_a * p_of_a) / p_of_b