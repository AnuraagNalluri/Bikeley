import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plots
# A = pd.read_csv("eD.csv")
# print(np.mean(A['light'][16200:19800]))
# print(np.mean(A['noise'][16200:19800]))
brightness = pd.read_csv("Brightness Penalty.csv")
crowdedness = pd.read_csv("Crowdedness Penalty.csv")
print(np.mean(brightness.iloc[9,1:]))
#print(crowdedness)
