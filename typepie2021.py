import pandas as pd
from itertools import chain
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
typename = []
types = []
test = []
tcount = []
df = pd.read_excel("D:\Github Python D1\PythonD1\Topsongs.xlsx")
for i in (df["Type"]):
 if i not in typename:
  typename.append(i)
for j in typename:
 types.append(len(df[df["Type"] == j]))
for k in range (len(typename)):
 print(typename[k],types[k])
 tcount.append(len(df[df["Type"] == j]))

colors = ("#ed281a","#ba5211","#edc61a","#59c72a","#7d2a79","#2ac7c2","#2aa0c7","#1e62ba","#e864d6","#c9c7c9","#65d9eb","#a665eb","#eba165","#a6eb65","#eb6582")
print(types)
plt.pie(types,labels=typename,startangle = 25,colors=colors,shadow=True)
plt.legend()
plt.title("Music Genre")
plt.show()
