import util

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
