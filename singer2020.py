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
for i in (df["Artist Names"]):
 if i not in allsingname:
  allsingname.append(i)
for j in allsingname:
 allsing.append(len(df[df["Artist Names"] == j]))
 singcount.append(len(df[df["Artist Names"] == j]))
for k in range (len(allsingname)):
 print(allsingname[k],allsing[k])
singcount.sort()
other = singcount[:24]
k = singcount[24:]
sumof = [sum(other)]
test.append(k)
test.append(sumof)
f = list(np.concatenate(test).flat)
labels = ["Camila Cabello","Cardi B","DOBERMAN INFINITY","Tilly Birds","Room39","Pop Pongkul","Atom Chanakan","Skillet","Maroon5","OneRepublic","Bodyslam","EXILE","Ed Sheeran","Shawn Mendes","Others"]
color = ["#e6e3dc","#d9d9d9","#dedede","#bfbfbf","#b5b5b5","#969696","#878787","#828282","#6b6b6b","#636363","#575757","#9c9c9c","#c9a540","#b5863a","#000000"]
explode = [0,0,0,0,0,0,0,0,0,0,0,0,0.2,0.2,0]
print(test)
print(f)
print(singcount)
plt.pie(f,explode=explode,colors= color,shadow=True,labels=labels,startangle=300)
plt.title("Artist Names")
plt.show()