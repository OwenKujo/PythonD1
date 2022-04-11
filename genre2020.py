import pandas as pd
from itertools import chain
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
allsingname = []
allsing = []
test = []
singcount = []
df = pd.read_excel("D:\Github Python D1\PythonD1\your_top_songs_2020.xlsx")
for i in (df["Type"]):
 if i not in allsingname:
  allsingname.append(i)
for j in allsingname:
 allsing.append(len(df[df["Type"] == j]))
for k in range (len(allsingname)):
 print(allsingname[k],allsing[k])
print(allsingname)
