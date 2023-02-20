import pandas as pd
import numpy as np
import seaborn as sns

def get_dataframe(csvFile="titanic_train.csv"):
    return pd.read_csv(csvFile)

def get_age_class_sex():
    """
    I want to find a dataframe that lists just the Age, Pclass, and Sex. Return a DataFrame with these columns
    """
    df = get_dataframe()
    df = df[['Age', 'Pclass', 'Sex']]
    return df
    pass

def get_age_class_sex_over_30():
    """
    Suppose I want the same 3 features, but this time, I only want to see people above the age of 30.
    Ultimately I would like visual of people over thirty, but let's just focus on getting a dataframe for now.
    """
    df = get_dataframe()
    df = df[['Age', 'Pclass', 'Sex']]
    df = df.loc[df['Age'] > 30]
    return df
    pass

def get_100th_person_info():
    """
    I want to access the data of the 100th person, how would I do that?
    """
    df = get_dataframe()
    df = df.iloc[[99]]

    dictionary = {}

    for col in df.columns:
        df1 = df[col]
        arr1 = list(df1)
        item1 = arr1[0]
        dictionary[col] = item1
    
    return dictionary

    pass


def calc_num_unique_ages():
    """
    Time to go back to the main dataframe, I would like to see how many unique ages there were, what function can I use to
    find that?
    """
    df = get_dataframe()
    count = df["Age"].nunique()
    return count
    pass

def get_cabin_nulls_and_shape():
    """
    I was going through the dataframe and noticed cabin had a lot of null values, how can I see how many null values there
    are? While I'm at it, let me see how big this dataframe is as a whole.
    
    This function should return a tuple of the form (number of null values in Cabin column, how many rows in the dataframe)
    """
    df = get_dataframe()
    rows = df.shape[0]
    count = df['Cabin'].isna().sum()
    return (count, rows)
    pass

def drop_cabin_col():
    """
    The Cabin column seems to have a lot of missing values. Drop this column and return the resulting dataframe
    """
    df = get_dataframe()
    df = df.drop('Cabin', axis=1)
    return df
    pass
  
def survived_within_class():
    """
    For each Pclass, return the proportion of people who survived. Round answer to nearest 3 decimal places
    Return tuple in the format (Pclass 1 survival proportion, Pclass 2 survival proportion, Pclass 3 survival proportion)
    If there is a ZeroDivisionError, return (-1,-1,-1)
    """
    df = get_dataframe()

    survived = [0, 0, 0]
    total = [0, 0, 0]

    for ind in df.index:
        total[df['Pclass'][ind] - 1] += 1
        if (df['Survived'][ind] == 1):
            survived[df['Pclass'][ind] - 1] += 1
    
    if (total[0] == 0 or total[1] == 0 or total[2] == 0):
        return (-1, -1, -1)

    fin = [survived[0] / total[0], survived[1] / total[1], survived[2] / total[2]]
    
    for i in range(len(fin)):
        fin[i] = round(fin[i] * 1000) / 1000    

    return fin
    pass