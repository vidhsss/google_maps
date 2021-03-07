import gmaps
import gmaps.datasets
gmaps.configure(api_key='AIzaSyAFRk860iZKdqoLnWQoXb--tB01Ri4poYE')

# Latitude-longitude pairs
geneva = (46.2, 6.1)
montreux = (46.4, 6.9)
zurich = (47.4, 8.5)

fig = gmaps.figure()
geneva2zurich = gmaps.directions_layer(geneva, zurich)
fig.add_layer(geneva2zurich)
fig
