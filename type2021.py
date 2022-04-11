import pandas as pd
from itertools import chain
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
typename = []
types = []
test = []
natcount = []
df = pd.read_excel("D:\Github Python D1\PythonD1\Topsongs.xlsx")
for i in (df["Type"]):
 if i not in typename:
  typename.append(i)
for j in typename:
 types.append(len(df[df["Type"] == j]))
for k in range (len(typename)):
 print(typename[k],types[k])