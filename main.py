import os.path
import folium
m = folium.Map(location=[28.496549448903032, 77.5127339839184], zoom_start=12)

overlay = os.path.join('JflexLearns', 'overlay.json')

folium.Marker([28.448712698875173, 77.47282923743266],
              popup="<h1> My University</h1><img src ='images.jpg' width=400px> <p> this is my university</p>",
              tooltip='Galgotias University',
              icon=folium.Icon(icon='heart', icon_color='red', color='green')).add_to(m)

folium.Marker([28.480427791536492, 77.4998366711647],
              popup="<h1>favorite place to eat </h1><img src ='rajaimages.jpg' width=400px> <p> this is my go-to eatery</p>",
              tooltip='Raja Dhabba',
              icon=folium.Icon(icon='cutlery', icon_color='blue', color='green')).add_to(m)

folium.Circle(
    location=(28.45686871832903, 77.49269307116471),
    radius=4500,
    popup='love the area',
    color='blue',
    fill=True,
    fill_color="blue"
).add_to(m)

# geojson overlay
folium.GeoJson(overlay, name='greater Noida').add_to(m)

m.save('map.html')