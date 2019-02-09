import numpy as np
import pandas as pd

data = pd.read_csv('rows.txt', delimiter = '\t')

data = np.subtract(data.max(axis=1),data.min(axis=1))
print(data.sum())
