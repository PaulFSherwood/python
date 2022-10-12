import pandas as pd
### Complete Python Pandas Data Science Tutorial! (Reaing CSV/Exel files, Sorting, Filter, Groupby)
### youtube.com/watch?v=vmEHCJofslg

##########################
### Potential problems ###
### does the file exist
### do you have permission to access the folder and file r/w?
### pathing (books says windows can fix the slashes)
### is the data valid
### corrupting a file / overwriting a file
### Large data set
### is the formating correct
### CSV files (can use pandas, and not worry too much)
### are you importing it correctly
### regular expressions (so powerful)
### missing columns
### Need to add columns
### working with dataclasses (don't understand, need research)



df = pd.read_csv('pokemon_data.csv')
# df = pd.read_csv('pokemon_data.txt, delimiter='\t')
# print(df.tail(2))

###################
## read headers ###
# print(df.columns)
# print(df['Name'].head(3))
# print(df['Generation'].head(3))

###########################
## print multiple colums ##
## Single: df['Name']      ||      Multiple: df[['Name', 'HP']]
# print(df['Sp. Def'])
# print(df[['Name', 'HP', 'Defense', 'Generation']].head(3))
# print(df.Attack.head(3))

#####################
## print out a row ##
# print(df.iloc[1])   # row 1
# print(df.iloc[4:6]) # row 4 to 6
# print(df)
# for index, row in df.iterrows():
# print(df.loc[df['Type 1'] == 'Grass'])  # don't need a loop with this
# print(df.loc[df['Sp. Def'] == 65])  # don't need a loop with this
        # print(index, row) ## row['Name']

####################################
## get a specific location (R, C) ##
# print(df.iloc[2, 1])  ## gets the Venusaur name

# get specific info from each row
# for index, row in df.iterrows(): ## info from each row
# for index, row in df.iloc[4:9].iterrows(): # info from a selection of rows
#         print(index, row['Name'])
# print('=#*-'*30)
# # you don't have to use .iloc[4:9] if you want all the rows, or you can change it to someother seleciton
# print(df.iloc[4:9].loc[df['Type 1'] == 'Fire'])

###############################
## sorting / describing data ##

## high level stats
# df.describe()

## sorting by alphabet
# print(df.sort_values(['Type 1', 'HP'], ascending=[True, False]))
# print(df.iloc[1:20].sort_values(['Type 1', 'HP'], ascending=[True, True]))

#################################
## making changes to your data ##
# (#) (Name) (Type 1) (Type 2) (HP) (Attack) (Defense) (Sp. Atk) (Sp. Def) (Speed) (Generation) (Legendary)

## Add a column
# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# print(df.head(3))

# ## remove a column
# df = df.drop(columns=['Total'])
# print(df.head(3))

# ## adding a column with iloc
df['Total'] = df.iloc[:,4:10].sum(axis=1)
# print(df.head(3))

# ## remove a column
# # df = df.drop(columns=['Total'])
# # print(df.head(3))

# ## move a column
# ## temp list for columns
cols = list(df.columns.values)
# ## select where the columns should go
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
# print(df.head(3))

## export data to a csv
# df.to_csv('modified.csv')
# df.to_excel('modified.xlsx', index=False)
# df.to_csv('modified.txt', index=False, sep='\t')
# # to remove the index when exporting
# df.to_csv('modified.csv', index=False)

####################
## Filtering Data ##
print('=#*-'*30)
# df.loc[  ## (df[column name] == name) ## & ## (df[column name] == name) ... etc
# df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Posion')]
# df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Posion')]
# print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)])
## can now save the data frame to something else and export it to a csv file.
# new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
# print(new_df)
# # new_df = new_df.reset_index()
# print('=#*-'*30)
# new_df.reset_index(drop=True, inplace=True)
# print(new_df)

# Filter out a name that you don't want.
# print(df.loc[df['Name'].str.contains('Mega')])   # show everythign where Name has Meag in it
# print(df.loc[~df['Name'].str.contains('Mega')])  # drop everything where Name has Mega in it

#########################
## regular expressions ##
import re
# flags
# ('fire|grass'), flags = re.I ## ignore case
# print(df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)])
# print(df.loc[df['Name'].str.contains('^Pi[a-z]*', flags=re.I, regex=True)])

## Conditional Changes
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
# print(df.loc['Type 1' == 'Flamer'].head(3))

# name and what you want        df.loc
# Conditions you need           [df['Type 1'] == 'Flamer]
# How many to print out         .head(4))
print(df.loc[df['Type 1'] == 'Flamer'].head(4))
df.loc[df['Type 1'] == 'Flamer', 'Type 1'] = 'Fire'
print(df.loc[df['Type 1'] == 'Fire'].head(4))

## change all fire to be legendary
df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True
print(df.loc[df['Type 1'] == 'Fire'].head(4))

df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['3', 'True']
print(df.head(5))

####################################
## Aggregate Statistics (Groupby) ##
df = pd.read_csv('modified.csv')
## group and sort
print(df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False).head(5))

########################################
## Working with large amounts of data ##
# for df in pd.read_csv('modified.csv', chunksize=5):
#         print("CHUCK DF")
#         print(df)

## pack to dataframes together
# new_df = pd.DataFrame(columns=df.columns)

# for df in pd.read_csv('modified.csv', chunksize=5):
#         results = df.groupby(['Type 1']).count()

#         new_df = pd.concat([new_df, results])
