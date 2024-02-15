import geocoder
g=geocoder.ip('me')
print(g.latlng)
print(g.city)
print(g.ip)
