import pandas as pd
data = pd.read_csv('try_data.csv') 
#for json data pd.read_json and extension of data format is .json
# for excel data pd.read_excel and the extension of data format is .xlsx
print(data)
print()

print (data.loc[[1,2,5],['name','salary']])

#Outputs Serially
''' name department  salary remarks
0  Bishal         It   10000     G:N
1     Ram       Manu   12000     G:G
2   Shyam       Serv   13000     G:G
3    Hari       food   14000     G:G
4    Gita     Pantry   15000     B:G
5    Sita         no   16000     B:B

    name  salary
1    Ram   12000
2  Shyam   13000
5   Sita   16000'''