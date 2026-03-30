# write a pandas program to merge two dataframes on a single column id

import pandas as pd

# Create first DataFrame
data1 = {
    'id': [1, 2, 3, 4],
    'name': ['Ankita', 'Rahul', 'Priya', 'Amit']
}

df1 = pd.DataFrame(data1)

# Create second DataFrame
data2 = {
    'id': [1, 2, 3, 5],
    'age': [20, 21, 19, 22]
}

df2 = pd.DataFrame(data2)

# Merge DataFrames on 'id'
merged_df = pd.merge(df1, df2, on='id')

# Display result
print("Merged DataFrame:")
print(merged_df)