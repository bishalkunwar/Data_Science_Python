import pandas as pd
import numpy as np

data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)
print("\n")


data1 = {'Name':['Bishal', 'Nishan', 'Ritesh', 'Passa'],'Age':[20,21,22,23]}
df = pd.DataFrame(data1, index=['rank1','rank2','rank3','rank4'])
print(df)

#Outputs Serially:
'''0    a
1    b
2    c
3    d
dtype: object

         Name  Age
rank1  Bishal   20
rank2  Nishan   21
rank3  Ritesh   22
rank4   Passa   23'''