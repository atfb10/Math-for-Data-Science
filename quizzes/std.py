import numpy as np


top = [220.1, 220.0, 220.0, 220.2, 220.1]
bottom = [220.1, 220.4, 220.2, 220.0, 220.1]

top_std = np.std(top)
bottom_std = np.std(bottom)

print(f'Top std: {top_std}')
print(f'Bottom std: {bottom_std}')