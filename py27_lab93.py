# file encoding ms950 reload
# file encoding utf-8 convert
# pip install folium
import folium
import pandas as pd

data1 = pd.read_csv('.//data//shilin_utf8.csv', sep=',')
print data1.shape
print data1.columns
print data1.head()
data1.columns = ['section', 'road', 'road_detail', 'lon', 'lat', 'extra']
print data1.head()

taipeiCenter = [25.089258, 121.524240]
zoom = 12
map_osm = folium.Map(location=taipeiCenter, zoom_start=zoom)

for i in range(len(data1)):
    coord = '[%.3f,%.3f]' % (data1.iloc[i, 4], data1.iloc[i, 3])
    display = '%s->%s' % (data1.iloc[i, 1], data1.iloc[i, 2])
    displayU = unicode(display, 'utf-8')
    print coord
    pos = [data1.iloc[i, 4], data1.iloc[i, 3]]
    defaultIcon = folium.Icon(color='green', icon='info-sign')
    message = '[%d]%s' % (i, displayU)
    folium.Marker(pos, icon=defaultIcon, popup=message).add_to(map_osm)

map_osm.save('.\\map\\orig.html')
