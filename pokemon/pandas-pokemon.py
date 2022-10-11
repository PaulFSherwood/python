import pandas as pd
### is the data valid
### is the formating correct
df = pd.read_csv('pokemon_data.csv')
# df = pd.read_csv('pokemon_data.txt, delimiter='\t')
# print(df.tail(2))

## read headers
print(df.columns)
# print(df['Name'].head(3))
# print(df['Generation'].head(3))

# print multiple colums
print(df[['Name', 'HP', 'Defense', 'Generation']].head(3))
# print(df.Attack.head(3))

# print out a row
print(df.iloc[4:6])
print(df)
for index, row in df.iterrows():
    # if c['Name'] == 'Venusaur':
    print(index, row) ## row['Name']

# get a specific location (R, C)
print(df.iloc[2, 1])