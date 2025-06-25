import pandas as pd
df1 = pd.DataFrame({
    'id':[1,2,3,4,5],
    'Name':['Akon','Bkon','Ckon','Dkon','Ekon'],
    'Subject':['A','B','C','D','E']},
    index = [11,22,33,44,55])
df2 = pd.DataFrame({
    'id':[8,2,7,4,6],
    'Name':['Fkon','Gkon','Hkon','Ikon','Jkon'],
    'Subejct':['F','G','H','I','J']},
    index = [11,22,33,44,55])
df3 = pd.DataFrame({
    'id':[9,2,1,4,11],
    'Name':['Kkon','Lmon','Nmon','Omon','Pmon'],
    'Subject':['Z','X','C','V','B']},
    index = [11,22,33,44,55])
df1_renamed = df1.add_suffix('_df1')
df2_renamed = df2.add_suffix('_df2')
res = pd.concat([df1_renamed,df2_renamed],axis=1)
print("After concatination::")
res['id']=df1['id']
print(res)
result = pd.merge(res,df3,on="id",how="inner")
print(result)