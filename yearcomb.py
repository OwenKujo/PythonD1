import pandas as pd
from itertools import chain
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
yearname = []
years = []
test = []
natcount = []
yearname2 = []
years2 = []
test2 = []
df = pd.read_excel("D:\Github Python D1\PythonD1\Book1.xlsx")
df2 = pd.read_excel("D:\Github Python D1\PythonD1\your_top_songs_2020.xlsx")
for i in (df["Year out"]):
 if i not in yearname:
  yearname.append(i)
yearname.sort()
for x in (df2["Year out"]):
 if x not in yearname2:
  yearname2.append(x)
yearname2.sort()
for j in yearname:
 years.append(len(df[df["Year out"] == j]))
for p in yearname2:
 years2.append(len(df2[df2["Year out"] == p]))
for k in range (len(yearname)):
 print(yearname[k],years[k])
for b in range (len(yearname2)):
 print(yearname2[b],years2[b])

oneninenine = years[:4]
k = years[4:]
sumof = [sum(oneninenine)]
test.append(sumof)
test.append(k)
oneninenine2 = years2[:8]
k2 = years2[8:]
sumof2= [sum(oneninenine2)]
test2.append(sumof2)
test2.append(k2)



f2 = list(np.concatenate(test2).flat)
f = list(np.concatenate(test).flat)

f.pop(0)
f2.pop(0)
natcount.append(f)
natcount.append(f2)
print(test)
print(f)
print(test2)
print(f2)
label=["2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"]
#plt.figure(figsize=(9, 3))
x_axis = np.arange(len(label))

plt.bar(x_axis -0.2,natcount[0],width=0.4,label="2020")
plt.bar(x_axis +0.2,natcount[1],width=0.4,label="2021")
plt.xticks(x_axis, label)
plt.xlabel("Year list")
plt.title("Release Year of all song in my Top2021&2020 playlist")
plt.legend()
plt.grid()
plt.show()