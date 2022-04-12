import pandas as pd
from itertools import chain
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
yearname = []
years = []
test = []
natcount = []
df = pd.read_excel("D:\Github Python D1\PythonD1\Book1.xlsx")
for i in (df["Year out"]):
 if i not in yearname:
  yearname.append(i)
yearname.sort()
for j in yearname:
 years.append(len(df[df["Year out"] == j]))
for k in range (len(yearname)):
 print(yearname[k],years[k])