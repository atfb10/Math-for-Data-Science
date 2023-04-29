import numpy as np

'''
problem statement: determine if both batches meet threshold of maximum standard deviation of .1
'''

batch1 = [220.1, 220.0, 220.0, 220.2, 220.1]
batch2 = [220.1, 220.4, 220.2, 220.0, 220.1]

batch1_std = np.std(batch1)
batch2_std = np.std(batch2)

print(f'Top std: {batch1_std}')
print(f'Bottom std: {batch2_std}') # This batch does not