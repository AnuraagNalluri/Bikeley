import subprocess
from subprocess import *
import main
subprocess.call('cp -r map.html map2.html', shell=True, cwd='/Users/shiva/desktop/bikeley/wallflower-pico-master/static')
html_str ="""<style>
html, body { height: 100%; margin: 0; padding: 0; }
#map { height: 100%; width: 100%; height: 100%; }
</style>
<div id="map"></div>
<script>
  function initMap() {
    var service = new google.maps.DirectionsService;
    var map = new google.maps.Map(document.getElementById('map'));

    // list of points
    var stations = [\n
"""

path = main.X
length = len(path)
i = 0
request_str = "var request = {\n"
waypoint_str = "waypoints: ["
for item in path:
    i += 1
    if i != length:
        html_str += "{lat: " + str(item[0]) + ", lng: " + str(item[1]) + "},\n"
    else:
        html_str += "{lat: " + str(item[0]) + ", lng: " + str(item[1]) + "}\n];"

# var first = new google.maps.LatLng(37.8761364, -122.2595716);
# var second = new google.maps.LatLng(37.8750948, -122.2601509);
# var third = new google.maps.LatLng(37.8728251, -122.262404);
# var origin_cor = new google.maps.LatLng(37.8761915, -122.2590835);
# var destination_cor = new google.maps.LatLng(37.8706188, -122.2657835);
#
# var request = {
# origin: origin_cor,
# destination: destination_cor,
# waypoints: [{location: first, stopover: true},
# {location: second, stopover: true},
# {location: third, stopover: true}],
# optimizeWaypoints: false,
# travelMode: google.maps.DirectionsTravelMode.BICYCLING
# };


with open("/Users/shiva/desktop/bikeley/wallflower-pico-master/static/map2.html", "r+") as f:
     old = f.read() # read everything in the file
     f.seek(0) # rewind
     f.write(html_str + old) # write the new line before
