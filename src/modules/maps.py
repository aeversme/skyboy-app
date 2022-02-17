import pydeck as pdk
import os

MAPBOX_API_KEY = os.environ['MAPBOX_API_KEY']


def create_flight_map(data):
    view_state = pdk.ViewState(latitude=float(data['GPS'][0][0]),
                               longitude=float(data['GPS'][0][1]),
                               zoom=16,
                               bearing=0,
                               pitch=30)

    # sources = {
    #     'mapbox-raster-dem': {
    #         'type': 'raster-dem',
    #         'url': 'mapbox://mapbox.mapbox-terrain-dem-v1'
    #     }
    # }
    #
    # layers = [
    #     {
    #         'id': 'sky',
    #         'type': 'sky',
    #         'paint': {
    #             'sky-type': 'atmosphere',
    #             'sky-atmosphere-sun': [0.0, 0.0],
    #             'sky-atmosphere-sun-intensity': 15
    #         }
    #     }
    # ]
    #
    # terrain = {
    #     'source': 'mapbox-raster-dem',
    #     'exaggeration': 2
    # }
    #
    # map_style = {
    #     'version': 8,
    #     'layers': layers,
    #     'sources': sources,
    #     'center': [
    #         float(data['GPS'][0][0]),
    #         float(data['GPS'][0][1])
    #     ],
    #     'pitch': 45,
    #     'terrain': terrain,
    #     'zoom': 16,
    #     'fog': {'range': [1, 10]}
    # }

    flight_map = pdk.Deck(map_provider='mapbox',
                          map_style=pdk.map_styles.SATELLITE,
                          api_keys={'mapbox': MAPBOX_API_KEY},
                          initial_view_state=view_state)
    return flight_map
