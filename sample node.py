import pandas as pd

def sample_node(df: pd.DataFrame, N: int, sampling_method: str, column_name=None,use_groupby = False, 
                groupby_columns= None, order=None) -> pd.DataFrame:
    """
    df: pandas dataframe
    N: value of N
    sampling_method: one of the sampling methods
    column_name: column name to sample records based on order
    use_groupby: to group by specified columns
    groupby_columns: specified column names to group by
    order: order to sample records based on
    """
    # Define the sampling method and parameters
    if sampling_method == "First N Rows":
        if use_groupby is True:
            sampled_df = df.groupby(groupby_columns).head(N)
        else:
            sampled_df = df.head(N)
    elif sampling_method == "Last N Rows":
        if use_groupby is True:
            sampled_df = df.groupby(groupby_columns).tail(N)
        else:
            sampled_df = df.tail(N)
    elif sampling_method == "1 of Every N Rows":
        if use_groupby is True:
            sampled_df = df.groupby(groupby_columns, group_keys=False).iloc[::N, :]
        else:
            sampled_df = df.iloc[::N, :]
    elif sampling_method == "First N% of rows":
        if use_groupby is True:
            sampled_df = df.groupby(groupby_columns).sample(frac=N/100)
        else:
            sampled_df = df.sample(frac=N/100)
    elif sampling_method == "1 in N Chance to Include Each Row":
        if use_groupby is True:
            raise ValueError("Can't use groupby with 1 in N Chance to Include Each Row sampling method.")
        else:
            sampled_df = df.sample(frac=1/N)
    elif sampling_method == "Sample records based on order":
        if column_name is None or order is None:
            raise ValueError("Both column_name and order must be specified for this method.")
        elif use_groupby is True:
            sampled_df = df.sort_values(by=column_name, ascending=order).groupby(groupby_columns).head(N)
        else:
            sampled_df = df.sort_values(by=column_name, ascending=order).head(N)
    else:
        raise ValueError("Invalid sampling method specified.")
    
    return sampled_df



df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
})

result = sample_node(df, 40, 'First N Rows', use_groupby=True, groupby_columns='City')

print(result)

