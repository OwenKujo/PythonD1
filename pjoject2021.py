import pandas as pd
from itertools import chain
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
allsingername = []
allsinger = []
test = []
singercount = []
df = pd.read_excel("D:\Github Python D1\PythonD1\Topsongs.xlsx")
for i in (df["Artist Names"]):
 if i not in allsingername:
  allsingername.append(i)
for j in allsingername:
 allsinger.append(len(df[df["Artist Names"] == j]))
for j in allsingername:
 singercount.append(len(df[df["Artist Names"] == j]))

allsinger.sort()
other = allsinger[:50]
k = allsinger[50:]
sumof = [sum(other)]
test.append(k)
test.append(sumof)

f = list(np.concatenate(test).flat)
labeln = ["Anne-Marie","Harry Styles","One Direction","Justin Bieber","KSI","Shawn Mendes","Ed Sheeran","Sam Smith","Taylor Swift","Other"]
explode = ( 0,0,0,0,0,0,0,0,0.2,0)
colors = ("#ed281a","#ba5211","#edc61a","#59c72a","#7d2a79","#2ac7c2","#2aa0c7","#1e62ba","#e864d6","#c9c7c9")
  #for x in range(len(singercount)):
    #print(allsingername[x],[x])
print(test)
  #print(allsinger)
print(f)
plt.pie(f,explode=explode,labels=labeln,shadow=True,startangle=5,colors=colors)
plt.title("Artist")
plt.legend()
plt.show()
  

#plt.pie(allsinger,labels=allsingername)
#plt.show()
#Ksi = allsinger.count("KSI")