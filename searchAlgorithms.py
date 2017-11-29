import util
import pandas as pd
import numpy as np
import time
import requests
import json
import random
import datetime
import serial
import pdb
import ast
import sys

brightness = pd.read_csv("Brightness Penalty.csv")
crowdedness = pd.read_csv("Crowdedness Penalty.csv")

base = 'http://127.0.0.1:5000'
network_id = 'local'
header = {}

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

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

sumz = 0
for key in od:
    if key != 'time' and is_number(od[key]):
        sumz += int(od[key])
        od[key] = int(od[key])
        #print(int(od[key]))
        #print(od['walkZones'])
    elif key == 'shortest' or key == 'uphill' or key == 'steepest' or key == 'walkZones' or key == 'crowds' or key == 'brightest':
        od[key] = 0

def bikeleyHeuristic(dist, walk, steepness, crowds, brightness):
    if steepness > 0:
        return od['shortest']*(dist/2112) + od['walkZones']*sys.maxint*walk + od['crowds']*(crowds) - od['steepest']*(steepness/14.52) + od['uphill']*((steepness**2)/(14.52**2)) + od['brightest']*brightness
    else:
        return od['shortest']*(dist/2112) + od['walkZones']*sys.maxint*walk + od['crowds']*(crowds) + od['uphill']*((steepness**2)/(14.52**2)) + od['brightest']*brightness

def trivialHeuristic(dist, walk, steepness, crowds, brightness):
    return dist + sys.maxint*walk

def badHeuristic(val):
    return -1*val

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    closed = []
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(),[],0),0)
    while fringe.isEmpty() != True:
        node = fringe.pop()
        if problem.isGoalState(node[0]):
            return node[1]
        if node[0] not in closed:
            closed.append(node[0])
            for child, edge, cost in problem.getSuccessors(node[0]):
                fringe.push((child, node[1]+[edge], node[2]+cost),node[2]+cost)
    return []

def AStarSearch(problem, heuristic):
    """Search the node of least total cost first as defined by the heuristic."""
    closed = []
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(),[],0),0)
    while fringe.isEmpty() != True:
        node = fringe.pop()
        if problem.isGoalState(node[0]):
            return node[1]
        if node[0] not in closed:
            closed.append(node[0])
            for child, edge, cost in problem.getSuccessors(node[0]):
                fringe.push((child, node[1]+[edge], node[2]+cost),heuristic(node[2]+cost))
    return []

def SteepSearch(problem, val, dictio):
    """Search the node of least total cost first as defined by the heuristic."""
    closed = []
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(),[],0),0)
    while fringe.isEmpty() != True:
        node = fringe.pop()
        if problem.isGoalState(node[0]):
            return node[1]
        if node[0] not in closed:
            closed.append(node[0])
            for child, edge, cost in problem.getSuccessors(node[0]):
                priority=node[2]+((dictio[node[0]].elevation-dictio[child].elevation)**2)
                fringe.push((child, node[1]+[edge], priority), val*priority)
    return []

def UphillSearch(problem, dictio):
    """Search the node of least total cost first as defined by the heuristic."""
    closed = []
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(),[],0),0)
    while fringe.isEmpty() != True:
        node = fringe.pop()
        if problem.isGoalState(node[0]):
            return node[1]
        if node[0] not in closed:
            closed.append(node[0])
            for child, edge, cost in problem.getSuccessors(node[0]):
                if (dictio[node[0]].elevation-dictio[child].elevation)>0:
                    priority=node[2]+((dictio[node[0]].elevation-dictio[child].elevation)**2)
                fringe.push((child, node[1]+[edge], priority), priority)
    return []

def BikeleySearch(problem, dictio, time, heuristic):
    """Search the node of least total cost first as defined by the heuristic."""
    closed = []
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(),[],0),0)
    while fringe.isEmpty() != True:
        node = fringe.pop()
        if problem.isGoalState(node[0]):
            return node[1]
        if node[0] not in closed:
            closed.append(node[0])
            for child, edge, cost in problem.getSuccessors(node[0]):
                if edge.walkOnly == True:
                    #print(od['walkZones'])
                    if od['walkZones'] > 0:
                        walkerino = 1
                    else:
                        walkerino = 0
                else:
                    walkerino = 0

                if time is not None:
                    brighterino = brightness.iloc[int(node[0][1:])-1,time+1]
                    crowderino = crowdedness.iloc[int(node[0][1:])-1,time+1]
                    if time <= 7 or time >= 18:
                        walkerino = 0

                else:
                    brighterino = np.mean(brightness.iloc[int(node[0][1:])-1,1:])
                    crowderino = np.mean(crowdedness.iloc[int(node[0][1:])-1,1:])

                priority = node[2] + heuristic(cost,walkerino,(dictio[child].elevation-dictio[node[0]].elevation),crowderino,brighterino)
                fringe.push((child, node[1]+[edge], priority), priority)
    return []
