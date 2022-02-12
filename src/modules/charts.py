import plotly.graph_objects as go
from plotly.subplots import make_subplots


def create_flight_dynamics_chart(data, unit):
    metric = {
        'alt_data': data['Alt(m)'],
        'alt_name': 'Alt (m)',
        'gs_data': data['GSpd(m/s)'],
        'gs_name': 'Ground Spd (m/s)',
        'vs_data': data['VSpd(m/s)'],
        'vs_name': 'Vert Spd (m/s)',
        'yaxis1_title': 'Altitude (m)',
        'yaxis2_title': 'Speed (m/s)'
    }
    imperial = {
        'alt_data': data['Alt(ft)'],
        'alt_name': 'Alt (ft)',
        'gs_data': data['GSpd(mph)'],
        'gs_name': 'Ground Spd (mph)',
        'vs_data': data['VSpd(mph)'],
        'vs_name': 'Vert Spd (mph)',
        'yaxis1_title': 'Altitude (ft)',
        'yaxis2_title': 'Speed (mph)'
    }
    unit_dict = metric
    if unit == 'imperial':
        unit_dict = imperial

    flight_dynamics = make_subplots(specs=[[{'secondary_y': True}]])
    flight_dynamics.add_trace(go.Scatter(x=data['Date'], y=unit_dict['alt_data'], name=unit_dict['alt_name'],
                                         hoverinfo='y'), secondary_y=False)
    flight_dynamics.add_trace(go.Scatter(x=data['Date'], y=unit_dict['gs_data'], name=unit_dict['gs_name'],
                                         hoverinfo='y'), secondary_y=True)
    flight_dynamics.add_trace(go.Scatter(x=data['Date'], y=unit_dict['vs_data'], name=unit_dict['vs_name'],
                                         hoverinfo='y'), secondary_y=True)
    flight_dynamics.update_layout(title_text='Flight Dynamics',
                                  legend=dict(
                                      orientation='h',
                                      yanchor='bottom',
                                      y=1.02,
                                      xanchor='right',
                                      x=1
                                  ))
    flight_dynamics.update_xaxes(title_text='Flight Time')
    flight_dynamics.update_yaxes(title_text=unit_dict['yaxis1_title'], secondary_y=False)
    flight_dynamics.update_yaxes(title_text=unit_dict['yaxis2_title'], secondary_y=True)
    return flight_dynamics


def create_battery_chart(data):
    battery_stats = make_subplots(specs=[[{'secondary_y': True}]])
    battery_stats.add_trace(go.Scatter(x=data['Date'], y=data['RxBt(V)'], name='Batt Voltage (V)', hoverinfo='y'),
                            secondary_y=False)
    battery_stats.add_trace(go.Scatter(x=data['Date'], y=data['Curr(A)'], name='Current (A)', hoverinfo='y'),
                            secondary_y=True)
    battery_stats.update_layout(title_text='Battery Stats',
                                legend=dict(
                                    orientation='h',
                                    yanchor='bottom',
                                    y=1.02,
                                    xanchor='right',
                                    x=1
                                ))
    battery_stats.update_xaxes(title_text='Flight Time')
    battery_stats.update_yaxes(title_text='Voltage (V)', secondary_y=False)
    battery_stats.update_yaxes(title_text='Current (A)', secondary_y=True)
    return battery_stats


def create_lq_chart(data):
    signal_stats = go.Figure()
    signal_stats.add_trace(go.Scatter(x=data['Date'], y=data['RQly(%)'], name='Rx LQ (%)', hoverinfo='y'))
    signal_stats.add_trace(go.Scatter(x=data['Date'], y=data['TQly(%)'], name='Tx LQ (%)', hoverinfo='y'))
    signal_stats.update_layout(title_text='Link Quality', legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='right',
        x=1
    ))
    signal_stats.update_xaxes(title_text='Flight Time')
    signal_stats.update_yaxes(title_text='Percent')
    return signal_stats


def create_signal_chart(data):
    signal_stats = go.Figure()
    signal_stats.add_trace(go.Scatter(x=data['Date'], y=data['1RSS(dB)'], name='Rx RSS (dB)', hoverinfo='y'))
    signal_stats.add_trace(go.Scatter(x=data['Date'], y=data['RSNR(dB)'], name='Rx SNR (db)', hoverinfo='y'))
    signal_stats.add_trace(go.Scatter(x=data['Date'], y=data['TRSS(dB)'], name='Tx RSS (dB)', hoverinfo='y'))
    signal_stats.add_trace(go.Scatter(x=data['Date'], y=data['TSNR(dB)'], name='Tx SNR (db)', hoverinfo='y'))
    signal_stats.update_layout(title_text='Signal Stats', legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='right',
        x=1
    ))
    signal_stats.update_xaxes(title_text='Flight Time')
    signal_stats.update_yaxes(title_text='Strength (dB)')
    return signal_stats
