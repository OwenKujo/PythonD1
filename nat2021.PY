import pandas as pd
from itertools import chain
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
allnatname = []
allnat = []
test = []
natcount = []
df = pd.read_excel("D:\Github Python D1\PythonD1\Topsongs.xlsx")
for i in (df["Nationality"]):
 if i not in allnatname:
  allnatname.append(i)
for j in allnatname:
 allnat.append(len(df[df["Nationality"] == j]))
for k in range (len(allnatname)):
 print(allnatname[k],allnat[k])
k = allnat[:3]
other = allnat[3:]
sumof = [sum(other)]

test.append(k)
test.append(sumof)
testf = list(np.concatenate(test).flat)
colors = ["#1d56b3","#cf1717","#e0e0e0","#10b31b","#d4d40f","#f2a0a0","#06188f","#45a4f7","#17e81b"]

labeln = ["English","Canadian","American","Other"]
print(testf)
plt.bar(allnatname,allnat,width=0.55,color = colors,)
plt.title("Artist Nationality in my top2021 playlist")
plt.ylabel('Number of song by artist nationality')
plt.xlabel("Nationality Name(s)")
plt.grid()
plt.show()

