import pandas as pd
from itertools import chain
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
allsingname2 = []
allsing2 = []
test2 = []
singcount2 = []
df2 = pd.read_excel("D:\Github Python D1\PythonD1\your_top_songs_2020.xlsx")
for x in (df2["Artist Names"]):
 if x not in allsingname2:
  allsingname2.append(x)
for r in allsingname2:
 allsing2.append(len(df2[df2["Artist Names"] == r]))
 singcount2.append(len(df2[df2["Artist Names"] == r]))
for b in range (len(allsingname2)):
 print(allsingname2[b],allsing2[b])
singcount2.sort()
other2 = singcount2[:24]
k2 = singcount2[24:]
sumof = [sum(other2)]
test2.append(k2)
test2.append(sumof)
f2 = list(np.concatenate(test2).flat)
labels = ["Camila Cabello","Cardi B","DOBERMAN INFINITY","Tilly Birds","Room39","Pop Pongkul","Atom Chanakan","Skillet","Maroon5","OneRepublic","Bodyslam","EXILE","Ed Sheeran","Shawn Mendes","Others"]
color = ["#e6e3dc","#d9d9d9","#dedede","#bfbfbf","#b5b5b5","#969696","#878787","#828282","#6b6b6b","#636363","#575757","#9c9c9c","#c9a540","#b5863a","#000000"]
explode = [0,0,0,0,0,0,0,0,0,0,0,0,0.2,0.2,0]
print(test2)
print(f2)
print(singcount2)
plt.pie(f2,explode=explode,colors= color,shadow=True,labels=labels,startangle=300,autopct='%1.1f%%')
plt.title("Artist Names")
plt.show()