import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plots
A = pd.read_csv("eD.csv")
print(np.mean(A['light'][16200:19800]))
print(np.mean(A['noise'][16200:19800]))
