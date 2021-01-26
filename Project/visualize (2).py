import gmplot
import sys
import pandas as pd
import webbrowser
import os

filename = sys.argv[1]
c_lat = sys.argv[2]
c_long = sys.argv[3]
df = pd.read_csv(filename)
longs = df['longitude'].to_numpy()
lats = df['latitude'].to_numpy()
w = df['score'].to_numpy() * 250
gmap = gmplot.GoogleMapPlotter(c_lat, c_long, 13)
gmap.heatmap(lats, longs, weights=w)
gmap.draw("output.html")
webbrowser.open('file://' + os.path.realpath("output.html"))
