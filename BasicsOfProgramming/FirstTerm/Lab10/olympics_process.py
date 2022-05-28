"""
OLYMPICS
"""
import pandas as pd

def read_data():
    """
    Creates dataframe from csv
    """
    df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
    for col in df.columns:
        if col[:2] == '01':
            df.rename(columns={col: 'Gold'+col[4:]}, inplace=True)
        elif col[:2] == '02':
            df.rename(columns={col: 'Silver'+col[4:]}, inplace=True)
        elif col[:2] == '03':
            df.rename(columns={col: 'Bronze'+col[4:]}, inplace=True)
        elif col[:1] == '№':
            df.rename(columns={col: '#'+col[1:]}, inplace=True)

    names_ids = df.index.str.split('\\s\\(') # split the index by '('

    df.index = names_ids.str[0]
    df['ID'] = names_ids.str[1].str[:3]

    df = df.drop('Totals')

    return df


def first_country(df):
    """
    Returns the first country from dataframe
    >>> first_country(read_data())[:1]
    # Summer    13
    Name: Afghanistan, dtype: object
    """
    return df.iloc[0]



def summer_biggest(df):
    """
    return the ribbon to the country that won the most gold medals in the\
summer games
    >>> summer_biggest(read_data())
    'United States'
    """
    return df[df.Gold == df.Gold.max()].index[0]

def difference_biggest(df):
    """
    return the ribbon with the country with the largest difference (modulus)\
between the number of gold medals at the summer and winter games
    >>> difference_biggest(read_data())
    'United States'
    """
    newdf = abs((df['Gold'] - df['Gold.1']))
    return newdf[newdf == newdf.max()].index[0]

def difference_biggest_relative(df):
    """
    return the ribbon with the country with the largest difference (per module)\
between the number of gold medals at the summer and winter games, relative to \
the total number of gold medals won by that country.
    >>> difference_biggest_relative(read_data())
    'Bulgaria'
    """
    exdf = df[(df["Gold"] != 0) & (df["Gold.1"] != 0)]
    newdf = abs((exdf['Gold'] - exdf['Gold.1'])/(exdf['Gold'] + exdf['Gold.1']))
    return newdf[newdf == newdf.max()].index[0]
def get_points(df):
    """
    must add a Points column to df and return only it
    >>> get_points(read_data())[:3]
    Afghanistan      2
    Algeria         27
    Argentina      130
    Name: Points, dtype: int64
    """
    df['Points'] = (df['Gold.2'] * 3) + (df['Silver.2'] * 2) + (df['Bronze.2'] * 1)
    return df['Points']
    