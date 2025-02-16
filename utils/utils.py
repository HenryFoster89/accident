def gruppa(df):
    return df.groupby('state_name').agg({'state_number': 'count'}).reset_index()