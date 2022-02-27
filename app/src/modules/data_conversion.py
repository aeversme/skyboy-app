import pandas as pd


def convert_gps_to_list(obj):
    return obj.str.split(' ')


def convert_df(df):
    df['Date'] = df[['Date', 'Time']].agg(' '.join, axis=1)
    df['Date'] = pd.to_datetime(df['Date'])
    df.drop(columns=['S1', '6P', 'S2', 'EX1', 'EX2', 'LS', 'RS', 'SA', 'SB', 'SC',
                     'SD', 'SE', 'SF', 'SG', 'SH', 'LSW'], inplace=True)
    df['GSpd(m/s)'] = round(df['GSpd(kmh)'] / 3.6, 1)
    df['GSpd(mph)'] = round(df['GSpd(kmh)'] / 1.609, 1)
    df['VSpd(mph)'] = round(df['VSpd(m/s)'] * 2.237, 1)
    df['Alt(ft)'] = round(df['Alt(m)'] * 3.281).astype(int)
    df['GPS'] = convert_gps_to_list(df['GPS'].astype('string'))
    df['lat'] = df.apply(lambda row: float(row.GPS[0]), axis=1)
    df['lon'] = df.apply(lambda row: float(row.GPS[1]), axis=1)
    df['3Dcoordinates'] = df.apply(lambda row: [row['lon'], row['lat'], row['Alt(m)']], axis=1)
    return df
