import pandas as pd
from itertools import chain
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
yearname = []
years = []
test = []
natcount = []
df = pd.read_excel("D:\Github Python D1\PythonD1\your_top_songs_2020.xlsx")
for i in (df["Year out"]):
 if i not in yearname:
  yearname.append(i)
yearname.sort()
for j in yearname:
 years.append(len(df[df["Year out"] == j]))
for k in range (len(yearname)):
 print(yearname[k],years[k])

oneninenine = years[:8]
k = years[8:]
sumof = [sum(oneninenine)]
test.append(sumof)
test.append(k)

f = list(np.concatenate(test).flat)
print(test)
print(f)
color = ("#ed281a","#ba5211","#edc61a","#59c72a","#7d2a79","#2ac7c2","#2aa0c7","#1e62ba","#e864d6","#c9c7c9","#45a4f7","#17e81b")
labels=["2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"]
f.pop(0)
#plt.figure(figsize=(9, 3))
plt.bar(labels,f)
plt.ylabel('Number of the song by year')
plt.xlabel("Year list")
plt.title("Release Year of all song in my Top2021 playlist")
plt.grid()
plt.show()