import pandas as pd


def convert_gps_to_tuple(obj):
    return obj.str.split(' ')


def convert_df(df):
    df['Date'] = df[['Date', 'Time']].agg(' '.join, axis=1)
    df['Date'] = pd.to_datetime(df['Date'])
    df.drop(columns=['Time', 'S1', '6P', 'S2', 'EX1', 'EX2', 'LS', 'RS', 'SA', 'SB', 'SC',
                     'SD', 'SE', 'SF', 'SG', 'SH', 'LSW'], inplace=True)
    df['GSpd(m/s)'] = round(df['GSpd(kmh)'] / 3.6, 1)
    df['GSpd(mph)'] = round(df['GSpd(kmh)'] / 1.609, 1)
    df['VSpd(mph)'] = round(df['VSpd(m/s)'] * 2.237, 1)
    df['Alt(ft)'] = round(df['Alt(m)'] * 3.281).astype(int)
    df['GPS'] = convert_gps_to_tuple(df['GPS'].astype('string'))
    return df
