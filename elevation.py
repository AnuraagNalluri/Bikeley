from json import loads
from time import sleep
from urllib2 import Request, urlopen
import pdb


latitude = [37.8745189,37.8741801,37.8737101,37.8743601,37.8746691,37.8758019,
37.8757003,37.875442,37.8750821,37.8737969,37.8738456,37.8738117,37.8753531,
37.8752048,37.8750948,37.8746755,37.8736,37.8734984,37.8755224,37.8738244,
37.8732739,37.8727658,37.8730834,37.8761364,37.8762931]

longitude = [-122.2600489,-122.2599954,-122.259534,-122.2588072,-122.2589492,
-122.2589869,-122.2583967,-122.2573721,-122.258032,-122.2582814,-122.2575224,
-122.2566533,-122.2583324,-122.2594213,-122.2601509,-122.2578442,-122.2587883,
-122.2596467,-122.256825,-122.255398,-122.2573024,-122.2586435,-122.2579461,
-122.2595716,-122.2585255]

locations = zip(latitude, longitude)


#locations=[(-122.2599953, 37.8745231), (50.449561, 30.525366)] #(lat,lon) pairs

#locations = locations[0:1]
# print(locations)
# print(locations[0])
# print(locations[1])
#pdb.set_trace()
elev = []
for loc in locations: 
    try:
#        request = Request('https://maps.googleapis.com/maps/api/elevation/json?locations={0},{1}&key=AIzaSyA_uROdHUg3zmRIkpPLyZ1P8aJKHSOYvvU'.format(loc[0],loc[1]))
        request = Request('https://maps.googleapis.com/maps/api/elevation/json?locations={0},{1}&key=AIzaSyBpoEofda2Svw5-CCBu6-WdVtX2kCYml8k'.format(loc[0],loc[1]))
        response = urlopen(request).read() 
        places = loads(response)
        print 'At {0} elevation is: {1}'.format(loc, places['results'][0]['elevation'])
        sleep(1)
        elev.append(places['results'][0]['elevation'])
    except:
        print 'Error for location: {0}'.format(loc)

print(elev)
pdb.set_trace()