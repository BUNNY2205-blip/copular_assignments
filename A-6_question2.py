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
#performing an inner merge on the given column
print("inner merge")
result = pd.merge(df1,df2,on=["id"],how="inner")
print(result)
#performing a left join
print("left join")
result1 = pd.merge(df1,df2,on=["id"],how='left')
print(result1)
#the misssing values are handeled using-> NaN, whenever there is a missing keyword or a key the compiler places NaN in the place of missing keyword output
#performing a right join 
print("Right join")
result2 = pd.merge(df1,df2,on=["id"],how='right')
print(result2)
#performing the join on the bases of index
df1_i=df1.set_index('id')
df2_i=df2.set_index('id')

result3 = df1_i.join(df2_i,how = 'outer',lsuffix='df1_i',rsuffix='df2_i')
print("index based join",result3)