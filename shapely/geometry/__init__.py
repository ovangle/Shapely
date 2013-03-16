"""Geometry classes and factories
"""

from shapely.geometry.geo import box, shape, asShape, mapping
from shapely.geometry.point import Point, asPoint
from shapely.geometry.linestring import LineString, asLineString
from shapely.geometry.polygon import Polygon, asPolygon
from shapely.geometry.multipoint import MultiPoint, asMultiPoint
from shapely.geometry.multilinestring import MultiLineString, asMultiLineString
from shapely.geometry.multipolygon import MultiPolygon, asMultiPolygon
from shapely.geometry.collection import GeometryCollection

__all__ = [
    'box', 'shape', 'asShape', 'Point', 'asPoint', 'LineString', 'asLineString',
    'Polygon', 'asPolygon', 'MultiPoint', 'asMultiPoint',
    'MultiLineString', 'asMultiLineString', 'MultiPolygon', 'asMultiPolygon',
    'GeometryCollection', 'mapping'
    ]


