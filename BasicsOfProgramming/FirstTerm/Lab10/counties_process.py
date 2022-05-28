"""
Counties
"""

import pandas as pd

def read_data(path_to_file):
    """
    Creates dataframe from scv
    """
    df = pd.read_csv(path_to_file)
    return df

def max_counties(df):
    """
    returns the name of the state with the largest number of counties
    >>> max_counties(read_data("census.csv"))
    'Texas'
    """
    return df['STNAME'].value_counts().nlargest(1).index[0]

def max_difference(df):
    """
    Returns the name of the county that contains the largest absolute change in\
population size during 2010-2015.
    >>> max_difference(read_data("census.csv"))
    'Harris County'
    """
    exdf = df[df["SUMLEV"] == 50]
    exdf['max value'] = exdf[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMA\
TE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].max(axis=1)
    exdf['min value'] = exdf[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMAT\
E2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].min(axis=1)
    exdf['ress'] = abs((exdf['max value'] - exdf['min value']))
    res = exdf[exdf.ress == exdf.ress.max()].loc[:, "CTYNAME"]
    return res.values[0]


def conditional_counties(df):
    """
    Return 5x2 DataFrame with columns = ['STNAME', 'CTYNAME']
    >>> conditional_counties(read_data("census.csv")).values[0][1]
    'Washington County'
    """
    exdf = df[(df["SUMLEV"] == 50) & ((df["REGION"] == 2) | (df["REGION"] == 1))]
    edf = exdf.loc[exdf['CTYNAME'].str.startswith('Washington')]
    nedf = edf[(df["POPESTIMATE2015"] > df["POPESTIMATE2014"])]
    return nedf[['STNAME', 'CTYNAME']]
