import pandas as pd
df1 = pd.DataFrame([[169, 58, 1.0],
                    [172, 73, 1.2],
                    [184, 82, 0.7]], columns=['height', 'weight', 'eye'])

df2 = pd.DataFrame([[176, 71, 10.8, 'M'],
                    [169, 62, 0.7, 'F'],
                    [156, 62, 1.3, 'M']], columns=['height', 'weight', 'eye', 'gender'])

df3 = pd.DataFrame([[3, 22], [2,21]], columns=['grade', 'age'])

df1
df2
df3

df12 =pd.concat([df1, df2]) 
df12 #row wise merge 
 #axis = 1 column wise
 #axis = 0 row wise this is default
df13 = pd.concat([df1, df3], axis=1)
df13 #column wise merge

