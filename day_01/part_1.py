import numpy as np

with open('input.txt', 'r') as f:
	frequences = np.array(f.readlines(), dtype=int)

print(f'Last frequence value: {np.cumsum(frequences)[-1]}')
