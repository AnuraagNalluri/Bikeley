import util

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
