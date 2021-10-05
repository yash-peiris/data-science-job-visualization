import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

df = pd.read_csv("data\ICT_listings.csv")
df['Jobs'] = 1

df_class = df[['jobSubClassification','Jobs','Year']]
# df_date = df_date.groupby(['Date'],as_index = False)['Jobs'].sum()
#print(df_class)

df_class.to_csv('Jobs-per-class.csv', index=False)