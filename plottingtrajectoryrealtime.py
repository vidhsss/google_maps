import os
os.environ["GOOGLE_API_KEY"]='AIzaSyAFRk860iZKdqoLnWQoXb--tB01Ri4poYE'
import pandas as pd
from bokeh.io import output_notebook
output_notebook()
bokeh_width, bokeh_height = 500,400
df = pd.read_csv('/Users/vipul1/Downloads/dvf_gex.csv')
lat,lon=28.556041,77.052718
api_key= os.environ['GOOGLE_API_KEY']
from bokeh.io import show
from bokeh.plotting import gmap
from bokeh.models import GMapOptions
from bokeh.models import ColumnDataSource
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
%matplotlib inline

def plot(lat, lng, zoom=11, map_type='roadmap'):
    gmap_options = GMapOptions(lat=lat, lng=lng, 
                               map_type=map_type, zoom=zoom)
    p = gmap(api_key, gmap_options, title='TRAJECTORY PLOT', 
             width=bokeh_width, height=bokeh_height)
    return p
p=plot(lat,lon)
for i in range (100):
    df = pd.read_csv('C:\\Users\\vipul\\Downloads\\dvf_gex.csv')
    source = ColumnDataSource(df)
    center = p.circle('lon', 'lat', size=4, alpha=0.2, color='black', source=source)
    m= p.line('lon', 'lat', line_width=4, color='blue', source=source)
    plt.pause(1e-17)
show(p)
