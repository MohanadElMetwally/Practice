import pandas as pd


def sort_table(dataframe, column_name, asc= True):
    # Sort the DataFrame ascendingly/descendingly by the specified column name
    return dataframe.sort_values(by=column_name, ascending= asc)

def select_columns(dataframe, cols):
    # Returns the DataFrame by the specified columns
    return dataframe[cols]

def identify_duplicates(dataframe, columns):
    # Sort the DataFrame by the specified columns
    sorted_df = dataframe.sort_values(by=columns)
    
    # Identify duplicates based on the sorted columns
    duplicates = sorted_df.duplicated(subset=columns, keep=False)
    
    # Create a new column 'Unique' to mark rows as unique or duplicates
    sorted_df['Unique'] = duplicates.map({True: 'Duplicated', False: 'Unique'})
    
    return sorted_df

def remove_duplicates(dataframe, columns):
    
    # Remove duplicates based on the specified columns
    deduplicated_df = dataframe.drop_duplicates(subset=columns, keep='first')
    
    return deduplicated_df

def concat_dataframes(data_frame1, data_frame2, row_position= None, ignore_idx= False):
    # Concatenate dataframes based on position
    if row_position:
        concatenated_dataframe= pd.concat([data_frame1,data_frame2], axis= 1, ignore_index= ignore_idx)
    else:
        concatenated_dataframe = pd.concat([data_frame1,data_frame2], ignore_index= ignore_idx)
    
    return concatenated_dataframe

def merge_dataframes(df1, df2, on_column= None, join_type= 'inner'):
    if on_column is not None:
        # Join based on common columns
        joined_df = pd.merge(df1, df2, on=on_column, how= join_type) # type: ignore (suppresses a warning)
    else:
        # Join based on column names
        joined_df = pd.merge(df1, df2, left_on=df1.columns.tolist(), right_on=df2.columns.tolist(), how= join_type) # type: ignore (suppresses a warning)
    
    return joined_df
