from cProfile import label
import pandas as pd
from itertools import chain
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
allsingname = []
allsing = []
test = []
singcount = []
typename = []
types = []
test2 = []
tcount = []
genrecomb = []
df2 = pd.read_excel("D:\Github Python D1\PythonD1\Topsongs.xlsx")
df = pd.read_excel("D:\Github Python D1\PythonD1\your_top_songs_2020.xlsx")
for i in (df["Type"]):
 if i not in allsingname:
  allsingname.append(i)

allsingname.pop(2)
allsingname.pop(4)

typename.append("J-pop")
typename.append("Thai-pop")
for j in allsingname:
 allsing.append(len(df[df["Type"] == j]))
for k in range (len(allsingname)):
 print(allsingname[k],allsing[k])
for x in (df2["Type"]):
 if x not in typename:
  typename.append(x)

for pp in range(5):
 typename.pop(3)
for tt in range(2):
 typename.pop(4)
for tt in range(2):
 typename.pop(6)
for p in typename:
 types.append(len(df2[df2["Type"] == p]))
for q in range (len(typename)):
 print(typename[q],types[q])
 tcount.append(len(df2[df2["Type"] == q]))


genrecomb.append(allsing)
genrecomb.append(types)

print(allsingname)
print(allsing)
print(typename)
print(types)
print(genrecomb)

x_axis = np.arange(len(allsingname))

plt.bar(x_axis -0.15,genrecomb[0],width=0.3,label=2020)
plt.bar(x_axis +0.15,genrecomb[1],width=0.3,label="2021")
plt.xticks(x_axis, allsingname)
plt.xlabel("Genre List")
plt.title("Genre Compare Of My Playlist")
plt.legend()
plt.grid()
plt.show()

