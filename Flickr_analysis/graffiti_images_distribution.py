import folium
import pandas as pd

# Read Dataset 
url = 'http://xujianzi.github.io/data/graffiti.csv'
gdata = pd.read_csv(url)
limit = 2000
data = gdata.iloc[0:limit, :]

# Instantiate a feature group for the incidents in the dataframe
events = folium.map.FeatureGroup()

# Add events to the maps feature
for lat, lng in zip(data.latitude, data.longitude):
    events.add_child(
        folium.CircleMarker(
            [lat, lng],
            radius=7, # define how big you want the circle markers to be
            color='yellow',
            fill=True,
            fill_color='red',
            fill_opacity=0.4
        )
    )

# Add events to map
nyc_map = folium.Map(location=[latitude, longitude], zoom_start=11)
nyc_map.add_child(events)
## save the file as html
#san_map.save(outfile= 'graffiti.html')