from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2): 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1 
    dlat = lat2 - lat1 

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 1000 
    return c * r

# Usage
lon1 = -3
lat1 = 5
lon2 = -5
lat2 = 3

print("Jarak antara Ulfi ke Aris yaitu",haversine(lat1, lon1, lat2, lon2))