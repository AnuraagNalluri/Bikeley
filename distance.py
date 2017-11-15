from math import sin, cos, sqrt, atan2, radians
import csv
import pandas as pd
import sqlite3
import time
import ast
import datetime
import numpy as np
import pdb
#from geopy.distance import vincenty
from json import loads
from time import sleep
from urllib2 import Request, urlopen

def des_index(conn_node):
	if conn_node[0] == 'B':
		return int(conn_node[1:]) - 1
	elif conn_node[0] == 'I':
		return int(conn_node[1:]) + 12 

# https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=40.6655101,-73.89188969999998&destinations=40.6905615%2C-73.9976592%7C&mode=bicycling&key=AIzaSyA_uROdHUg3zmRIkpPLyZ1P8aJKHSOYvvU
# https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=37.8745231,-122.2599953&destinations=37.8741759%2C--122.2599632%7C&key=AIzaSyBpoEofda2Svw5-CCBu6-WdVtX2kCYml8k


# rack_lat = [37.8745231,37.8741759,37.8737186,37.8742267,37.874811,
# 37.8760306,37.8756918,37.8757003,37.8755436,37.8750821,37.8735746,
# 37.8737609,37.8739472]

# int_lat = [37.8753531,37.8752048,37.8750948,37.874629,
# 37.8746967,37.8746755,37.8738964,37.8738032,37.8736932,37.8736254,
# 37.8734984,37.8755224,37.8738244,37.8739853,37.8732739,37.8727658,
# 37.8735619,37.8749254,37.8730834,37.8750228,37.8761364,37.8760475,
# 37.8762931,37.8764752]


# rack_long = [-122.2599953,-122.2599632,-122.259534,-122.2588903,
# -122.2588795,-122.2590297,-122.2589654,-122.2583109,-122.2573185,
# -122.258032,-122.2581822,-122.2575921,-122.2565782]

# int_long = [-122.2583324,-122.2594213,-122.2601509,-122.2600758,
# -122.2589493,-122.2578442,-122.2575116,-122.2582841,-122.2598612,
# -122.2587883,-122.2596467,-122.256825,-122.255398,-122.2567874,
# -122.2573024,-122.2586435,-122.2565728,-122.2584826,-122.2579461,
# -122.2567981,-122.2595716,-122.2603333,-122.2585255,-122.2570342]




#locations=[(-122.2599953, 37.8745231), (50.449561, 30.525366)] #(lat,lon) pairs
# rack_loc = zip(rack_lat, rack_long)
# int_loc = zip(int_lat, int_long)
# #locations = rack_loc + int_loc
# print locations

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



dic = {
	1: [2,5,15], 2: [1,3,18], 3: [2,17,18], 
	4: [5,10], 5: [1,4], 6: [13,14,24,25],
	7: [13,25], 8: [13,19], 9: [13,16],
	10: [4,11,17,23], 11: [10,12,16,21], 12: [11,20,21],
	13: [6,7,8,9,14], 14: [6,13,15,24], 15: [1,14,24],
	16: [9,11], 17: [3,10,18,22], 18: [2,3,17,22],
	19: [8,20,25], 20: [12,19,21], 21: [11,12,20,23],
	22: [17,18,23], 23: [10,21,22], 24: [6,14,15,25],
	25: [6,7,19,24]
	}
for i in range(0, len(dic[1])):
	print dic[1][i]
#pdb.set_trace()

#pdb.set_trace()

#https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=40.6655101,-73.89188969999998&destinations=40.6905615%2C-73.9976592%7C&key=AIzaSyA_uROdHUg3zmRIkpPLyZ1P8aJKHSOYvvU
# orr = []
# orr.append(37.8745231)
# orr.append(-122.2599953)

# des = []
# des.append(37.8741759)
# des.append(-122.2599632)

ls = []

#pdb.set_trace()

# pdb.set_trace()
#print 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={0},{1}&destinations={2}%2C{3}%7C&mode=bicycling&key=AIzaSyBpoEofda2Svw5-CCBu6-WdVtX2kCYml8k'.format(orr[0],orr[1],des[0],des[1])

for i in range(0, len(locations)):
	orr = locations[i]
	print 'Origin:' + str(orr)
	duration = [''] * 25
	for j in range(0, len(dic[i+1])):
		des_index = dic[i+1][j]
		des = locations[des_index-1]
		print str(orr) + ' to ' + str(des_index) + ': ' + str(des)
		#des_ind_num = des_index(conn_node)
		
		# print 'Destination: ' + str(des)
		
		try:
		   	#request = Request('https://maps.googleapis.com/maps/api/elevation/json?locations={0},{1}&key=AIzaSyA_uROdHUg3zmRIkpPLyZ1P8aJKHSOYvvU'.format(loc[0],loc[1]))
		    # pdb.set_trace()
		    request = Request('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={0},{1}&destinations={2}%2C{3}%7C&mode=bicycling&key=AIzaSyBpoEofda2Svw5-CCBu6-WdVtX2kCYml8k'.format(orr[0],orr[1],des[0],des[1]))
		    print request
		    # https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=40.6655101,-73.89188969999998&destinations=40.6905615%2C-73.9976592%7C&key=AIzaSyA_uROdHUg3zmRIkpPLyZ1P8aJKHSOYvvU
		    # request = Request('https://maps.googleapis.com/maps/api/elevation/json?locations={0},{1}&key=AIzaSyBpoEofda2Svw5-CCBu6-WdVtX2kCYml8k'.format(loc[0],loc[1]))
		    response = urlopen(request).read() 
		    places = loads(response)
		    dur = str(places['rows'][0]['elements'][0]['distance']['text'])
		    print 'duration is: ' + dur
		    #print 'At {0} elevation is: {1}'.format(loc, places['results'][0]['elevation'])
		    sleep(1)
		    duration[des_index-1] = dur
		    


		    

		except:
		    print 'Error for location: {0}'.format(orr[0]) 

	ls.append(duration)
	
with open("distance_output_11_15.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerows(ls)

pdb.set_trace()
# newport_ri = (37.8745231, -122.2599953)
# cleveland_oh = (37.8741759, -122.2599632)
# print(vincenty(newport_ri, cleveland_oh).miles)

# pdb.set_trace()

df = pd.read_csv("testbed.csv")

# R = 6371.0

# lat1 = df["Latitude"]
# lat2 = df.iloc[0,1]

# lon1 = df["Longitude"]
# lon2 = df.iloc[0,2]

# dlat = radians(abs(lat2 - lat1))
# dlon = radians(abs(lon2 - lon1))

#a = sin(radians(abs(df.iloc[0,1] - df["Latitude"]))/2)**2 + cos(df.iloc[0,1]) * sin(radians(abs(df.iloc[0,2] - df["Longitude"]))/2)**2
# c = R * 2 * atan2(sqrt(sin(radians(abs(df.iloc[0,1] - df["Latitude"]))/2)**2 + cos(df.iloc[0,1]) 
# 	* sin(radians(abs(df.iloc[0,2] - df["Longitude"]))/2)**2), 
# 	sqrt(1-(sin(radians(abs(df.iloc[0,1] - df["Latitude"]))/2)**2 + cos(df.iloc[0,1]) 
# 		* sin(radians(abs(df.iloc[0,2] - df["Longitude"]))/2)**2)))

# distance = R*c

# df["B1"] = df["B1"].astype(float)
# pdb.set_trace()

# df["B1"] = R * 2 * cos(df.iloc[0,1])
# pdb.set_trace()
rad = 0.0174533
df["B1"] = R * sqrt ((rad * (df.iloc[0,2] - df["Longitude"]) * cos(0.5 * rad * (df.iloc[0,1] + df["Latitude"])))**2 * 
(df.iloc[0,1] - df["Latitude"]))**2

pdb.set_trace()

df["B1"] = R * 2 * float(atan2(sqrt(sin(radians(abs(df.iloc[0,1] - df["Latitude"]))/2)**2 + cos(df.iloc[0,1]) 
	* sin(radians(abs(df.iloc[0,2] - df["Longitude"]))/2)**2), 
	sqrt(1-(sin(radians(abs(df.iloc[0,1] - df["Latitude"]))/2)**2 + cos(df.iloc[0,1]) 
		* sin(radians(abs(df.iloc[0,2] - df["Longitude"]))/2)**2))))


# def distance_calc(x):
# 	lat1 = df["Latitude"]
# 	lat2 = df.iloc[0,1]

# 	lon1 = df["Longitude"]
# 	lon2 = df.iloc[0,2]

# 	return lat1-lat2


pdb.set_trace()
#-------------------------------------------------
# # to sql
# current_time = "testbed_db"
# conn = sqlite3.connect(current_time + '.db')
# c = conn.cursor()
# df.to_sql("raw", conn, if_exists = 'replace')
#-------------------------------------------------