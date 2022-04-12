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
allsingname.pop(2)
for j in allsingname:
 allsing.append(len(df[df["Type"] == j]))
for k in range (len(allsingname)):
 print(allsingname[k],allsing[k])
print(allsingname)
explode = [0,0,0.2,0,0,0,0]
color = ["#ed281a","#ebd61c","#2aa0c7","#59c72a","#7d2a79","#2ac7c2","#e864d6"]
plt.pie(allsing,labels=allsingname,colors=color,shadow=True,explode=explode)
plt.show()
