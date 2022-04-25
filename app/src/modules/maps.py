import pydeck as pdk

# The Mapbox API key is read from the .streamlit/config.toml file.


def aggregate_path(column):
    path_dict = {'path': [i for i in column]}
    return [path_dict]


def create_flight_map(data):
    view_state = pdk.ViewState(latitude=data['lat'].mean(),
                               longitude=data['lon'].mean(),
                               zoom=15,
                               bearing=0,
                               pitch=40)

    flight_path = aggregate_path(data['3Dcoordinates'])

    path_layer = pdk.Layer(
        'PathLayer',
        flight_path,
        width_min_pixels=2,
        get_path='path',
        get_color=[255, 255, 0, 255],
        get_width=2
    )

    layers = [path_layer]

    flight_map = pdk.Deck(map_provider='mapbox',
                          layers=layers,
                          map_style=pdk.map_styles.SATELLITE,
                          initial_view_state=view_state)
    return flight_map
