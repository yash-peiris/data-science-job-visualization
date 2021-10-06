# import pandas as pd
# pd.options.mode.chained_assignment = None  # default='warn'

# df = pd.read_csv("data\listings2019_2021.csv")
# df['Jobs'] = 1

# df_date = df[['Date','Jobs']]
# df_date = df_date.groupby(['Date'],as_index = False)['Jobs'].sum()
# print(df_date)

# df_date.to_csv('Jobs-per-date.csv', index=False)

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

df = pd.read_csv("data\State-Time-Breakdown.csv")
df['Jobs'] = 1

df_date = df[['Date','state','Jobs']]
# df_date = df_date.groupby(['Date'],as_index = False)['Jobs'].sum()
print(df_date)

df_date.to_csv('Jobs-per-date-state.csv', index=False)