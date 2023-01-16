import fiona
from shapely.geometry import mapping, shape, LineString, MultiPoint, Point

def should_keep_road(road):
    if ('highway' in road['properties']
            and road['properties']['highway'] is not None
            and road['properties']['highway'] != 'path'
            and road['properties']['highway'] != 'footway'):
        return True
    if ('class' not in road['properties'] or road['properties']['class'] == 'highway'
            and road['properties']['bridge'] == 0
            and road['properties']['tunnel'] == 0):
        return True
    return False


shp_file = fiona.open('./map.osm')
roads = []
for road in shp_file:
    if should_keep_road(road):
        roads.append(shape(road['geometry']))



