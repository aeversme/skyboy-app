import pandas as pd


def convert_gps_to_tuple(obj):
    return obj.str.split(' ')


def convert_df(df):
    df['Date'] = df[['Date', 'Time']].agg(' '.join, axis=1)
    df['Date'] = pd.to_datetime(df['Date'])
    df['GSpd(m/s)'] = round(df['GSpd(kmh)'] / 3.6, 1)
    df['GPS'] = convert_gps_to_tuple(df['GPS'].astype('string'))
    df.drop(columns=['Time'], inplace=True)
    return df
