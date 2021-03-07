import gmaps
gmaps.configure(api_key='AIzaSyAFRk860iZKdqoLnWQoXb--tB01Ri4poYE')

marker_locations = [
    
    (28.53333, 77.033327),
    (28.566672, 77.033331),
    (28.556041, 77.052718),
    (28.516671, 77.0833302),
    (28.503328, 77.096)
]

fig=gmaps.figure(center=(28.530181,77.050888), zoom_level=12)
markers = gmaps.marker_layer(marker_locations)
for i in range(4):
    line=gmaps.Line(start=marker_locations[i],end=marker_locations[i+1],stroke_color=(0,0,0,0.9),stroke_weight=4.0)
    drawing=gmaps.drawing_layer(features=[line])
    fig.add_layer(drawing)
fig.add_layer(markers)
fig
