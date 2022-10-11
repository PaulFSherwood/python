import pandas as pd
### is the data valid
### is the formating correct
df = pd.read_csv('pokemon_data.csv')
# df = pd.read_csv('pokemon_data.txt, delimiter='\t')
# print(df.tail(2))

## read headers
# print(df.columns)
# print(df['Name'].head(3))
# print(df['Generation'].head(3))

# print multiple colums
# print(df['Sp. Def'])
# print(df[['Name', 'HP', 'Defense', 'Generation']].head(3))
# print(df.Attack.head(3))

# print out a row
# print(df.iloc[4:6])
# print(df)
# for index, row in df.iterrows():
# print(df.loc[df['Type 1'] == 'Grass'])  # don't need a loop with this
# print(df.loc[df['Sp. Def'] == 65])  # don't need a loop with this
        # print(index, row) ## row['Name']

# get a specific location (R, C)
# print(df.iloc[2, 1])

## sorting / describing data
# df.describe()

print(df.sort_values(['Type 1', 'HP'], ascending=[True, False]))