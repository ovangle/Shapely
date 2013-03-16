# TODO: allow for implementations using other than GEOS

from shapely.geos import lgeos

def explain_validity(ob):
    valid = lgeos.GEOSisValidReason(ob._geom)
    return valid.decode('ascii')

