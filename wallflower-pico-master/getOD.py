"""
    Created 10/13
    by Chris Chin

    1) GET most recent Cosine and Temperature values uploaded by
       ListenAndSend.py
    
    2) If either Cosine or Temperature have changed since the last
       GET request, calculate the product of the two and upload the
       resulting value to For-Arduino stream, which ListenAndSend.py 
       will transfer to Arduino
    
"""
import time
import requests
import json
import random
import datetime
import serial
import pdb
import ast

#pdb.set_trace()

delay = 1*5 # Delay in seconds


base = 'http://127.0.0.1:5000'
network_id = 'local'
header = {}
   

# Run once at the start
def setup():
    try:
        print "Setup"
    except:
        print "Setup Error"
    return

# Run continuously forever
def loop():
    try: 
        ##### Step 1)
        ##### GET Origin and Destination

        # Retrieve most recent OD values
        print("Start retrieving OD")
        query = {}
        endpoint = '/networks/'+network_id+'/objects/obj-OD-pairs/streams/stm-form-input/points'
        response = requests.request('GET', base + endpoint, params=query, headers=header, timeout=120 )
        #print response
        resp = json.loads( response.text )
        #print "response ", resp
        od = resp['points'][0]['value']  
        print "Done Retrieving OD: "

        print type(od), od
        od = ast.literal_eval(od)
        print type(od), od
        
    except:
        print "Error"

    time.sleep(5) # GET requests every 5 sec
    return 

# Run continuously forever
# with a delay between calls
def delayed_loop():
    print "Delayed Loop"

# Run once at the end
def close():
    try:
        print "Close"
    except:
        print "Close Error"
    
# Program Structure    
def main():
    # Call setup function
    setup()
    # Set start time
    nextLoop = time.time()
    while(True):
        # Try loop() and delayed_loop()
        try:
            loop()
            if time.time() > nextLoop:
                # If next loop time has passed...
                nextLoop = time.time() + delay
                delayed_loop()
        except KeyboardInterrupt:
            # If user enters "Ctrl + C", break while loop
            break
        except:
            # Catch all errors
            print "Unexpected error."
            time.sleep(5)
    # Call close function
    close()

# Run the program
main()
