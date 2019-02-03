from itertools import cycle
import numpy as np

with open('input.txt', 'r') as f:
	changes = np.array(f.readlines(), dtype=int)

frequency = 0
historical_frequencies = {frequency}
for change in cycle(changes):
	frequency += change
	if frequency in historical_frequencies:
		break
	historical_frequencies.add(frequency)

print(f'First repeated frequency: {frequency}')  
