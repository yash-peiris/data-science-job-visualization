import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

df = pd.read_csv("data\listings2019_2021.csv")
df['Jobs'] = 1

df_class = df[['jobClassification','Jobs']]
# df_date = df_date.groupby(['Date'],as_index = False)['Jobs'].sum()
#print(df_class)

df_class.to_csv('Jobs-per-class.csv', index=False)