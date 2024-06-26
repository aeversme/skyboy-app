import streamlit as st
import pandas as pd
from PIL import Image
from src.modules import data_conversion as dc
from src.modules import charts as ch
from src.modules import metrics as mt
from src.modules import maps as mp
from src.modules import demo

# Set the server address to listen on all network interfaces
st.set_option('server.address', '0.0.0.0')


@st.cache
def load_data(file):
    data = pd.read_csv(file)
    converted_data = dc.convert_df(data)
    return converted_data


def display_flight(data, unit, alt, spd):
    st.subheader('Flight Metrics')
    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric('Date', mt.get_date(data['Date']))
    col2.metric('Time', mt.get_time(data['Date']))
    col3.metric('Flight Length', mt.get_flight_length(data['Date']))
    col4.metric('Flight Distance', mt.calc_flight_distance(data['lat'], data['lon'], unit))
    col5.metric('Max Distance from Home', mt.calc_max_distance(data['lat'], data['lon'], unit))

    col1.metric('Max Altitude', mt.get_max_altitude(data[alt], unit))
    col2.metric('Max Ground Speed', mt.get_max_ground_speed(data[spd], unit))
    col3.metric('Max Current Draw', mt.get_max_current(data['Curr(A)']))
    col4.metric('Capacity Used', mt.get_capacity_used(data['Capa(mAh)']))
    col5.metric('Transmitter Power', mt.get_tx_power(data['TPWR(mW)']))

    st.subheader('3D Flight Map')
    st.markdown('_Drag to pan. Hold `SHIFT` and drag to rotate. Scroll to zoom._')
    flight_map = mp.create_flight_map(data)
    st.pydeck_chart(flight_map)

    st.subheader('Flight Charts')
    chartcol1, chartcol2 = st.columns(2)
    chartcol1_count = 0
    chartcol2_count = 0

    st.sidebar.markdown('_Charts:_')
    if st.sidebar.checkbox('Flight dynamics', value=True):
        chartcol1.plotly_chart(ch.create_flight_dynamics_chart(data, unit))
        chartcol1_count += 1

    if st.sidebar.checkbox('Battery stats', value=True):
        if chartcol1_count > 0:
            chartcol2.plotly_chart(ch.create_battery_chart(data))
            chartcol2_count += 1
        else:
            chartcol1.plotly_chart(ch.create_battery_chart(data))
            chartcol1_count += 1

    if st.sidebar.checkbox('Link quality', value=True):
        if chartcol1_count == 1 and chartcol2_count == 0:
            chartcol2.plotly_chart(ch.create_lq_chart(data))
            chartcol2_count += 1
        else:
            chartcol1.plotly_chart(ch.create_lq_chart(data))
            chartcol1_count += 1

    if st.sidebar.checkbox('Signal stats', value=True):
        if (chartcol1_count == 1 and chartcol2_count == 0) or (chartcol1_count == 2 and chartcol2_count == 1):
            chartcol2.plotly_chart(ch.create_signal_chart(data))
        else:
            chartcol1.plotly_chart(ch.create_signal_chart(data))


subtitle_markdown = """
_A quadcopter telemetry log visualization app_
***
"""

initial_markdown = """
**Skyboy will display:**
* metrics from your flight: distance, time, max altitude, and more;
* an interactive map with a trace of your flight's GPS path;
* and charts for analyzing related data.

Choose from metric or Imperial units.
"""

update_markdown = """
_Latest update: May 22, 2022_
"""

if 'demomode' not in st.session_state:
    st.session_state.demomode = False

metrics_image = Image.open('src/images/metrics.png')
map_image = Image.open('src/images/map.jpg')
chart_image = Image.open('src/images/chart.png')

st.set_page_config(page_title='Skyboy Quad Telemetry App', layout='wide')

st.title('Skyboy')
st.markdown(subtitle_markdown)

st.sidebar.title('Skyboy Utilities')
demo_button = st.sidebar.button("Demo Skyboy")
if demo_button:
    demo.get_demo_telemetry()
    st.session_state.demomode = True
uploaded_file = st.sidebar.file_uploader('Upload a telemetry log:', type=['csv'])

if not uploaded_file and not st.session_state.demomode:
    col1, col2 = st.columns(2)
    col1.write(initial_markdown)
    col1.subheader("Upload a telemetry log in the sidebar to get started!")
    col2.image(metrics_image)
    col2.image(map_image)
    col2.image(chart_image)
    st.sidebar.caption("NB: Uploaded files are stored in memory and will not persist after the app is closed. Each "
                       "instance of the app is independent of every other instance.")

if st.session_state.demomode or (uploaded_file is not None):
    st.sidebar.markdown('_Data processing status:_')
    data_load_state = st.sidebar.text('Loading data...')

    if uploaded_file:
        flight_data = load_data(uploaded_file)
        st.session_state.demomode = False
    else:
        flight_data = load_data('demo-telemetry.csv')

    data_load_state.text('Loading data and caching... done!')

    if st.sidebar.checkbox('Show raw flight data'):
        st.subheader('Raw flight data')
        st.dataframe(flight_data)

    user_unit = 'metric'
    alt_label = 'Alt(m)'
    spd_label = 'GSpd(m/s)'
    if st.sidebar.checkbox('Use Imperial units'):
        user_unit = 'imperial'
        alt_label = 'Alt(ft)'
        spd_label = 'GSpd(mph)'

    display_flight(flight_data, user_unit, alt_label, spd_label)


st.sidebar.write(update_markdown)
