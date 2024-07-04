def transform_data(df):
    df_cleaned=df.drop_duplicates(keep='first')
    return df_cleaned


