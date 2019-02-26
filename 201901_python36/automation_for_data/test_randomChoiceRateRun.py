import numpy as np

DICT_VAR = {'A': 100, 'B': 1000, 'C': 5000, 'D': 8000}

keys, weights = zip(*DICT_VAR.items())
probs = np.array(weights, dtype=float) / float(sum(weights))
#sample_np = np.random.choice(keys, 2, p=probs)
sample_np = np.random.choice(keys, 1, p=probs)
sample = [str(val) for val in sample_np]

print(str(sample).replace('[','').replace(']',''))