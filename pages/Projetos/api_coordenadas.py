from geopy.geocoders import Nominatim
import plotly.graph_objects as go

def localizar_coordenadas(bairro, estado, uf, cep):
    geolocator = Nominatim(user_agent="geograpy_example")
    local = f"{bairro}, {estado} - {uf}, {cep}"
    location = geolocator.geocode(local)
    latitude = location.latitude
    longitude = location.longitude
    fig = go.Figure(go.Scattermap(
        lat=[latitude],
        lon=[longitude],
        mode='markers',
        marker=go.scattermap.Marker(size=14),
        text=bairro,))
    fig.update_layout(map=dict(center=go.layout.map.Center(
            lat=latitude,
            lon=longitude), zoom=14))

    return fig