import pandas as pd

def format(dataframe: pd.DataFrame, column: str, rule):
    # Applies formatting rules to a specific column.
    return dataframe[column].apply(rule)

def remove_duplicates(dataframe: pd.DataFrame, columns=None):
    # Removes duplicate rows.
    return dataframe.drop_duplicates(subset=columns) # subset: a list of columns to consider when identifying duplicates.

def resolve_inconsistencies(dataframe: pd.DataFrame, column: str, map: dict):
    # Resolves inconsistencies in a specific column using a mapping dictionary.
    return dataframe[column].replace(map)



