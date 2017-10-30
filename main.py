import util
import searchAlgorithms

class SearchProblem:
    """
    This class outlines the structure of a search problem
    """
    def __init__(self, start, end, graph):
        self.startState = start
        self.goalState = end
        self.graph = graph

    def getStartState(self):
        return self.startState

    def isGoalState(self, state):
        return state==self.goalState

    def getSuccessors(self, state):
        successors=[]
        for edge in nodeDict[state].getEdges():
            successors.append((edge.end, edge, edge.weight))
        return successors

class Node:
    def __init__(self, name, edges):
        self.name = name
        self.edges = edges

    def getEdges(self):
        return self.edges

class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

class Graph:
    def __init__(self, nodeDict):
        self.nodes = nodeDict

def pathToString(path):
    for edge in path:
        print(edge.start + "  -->  " + edge.end)

e1 = Edge("A","C",1)
e2 = Edge("A","B",2)
e3 = Edge("C","D",3)
e4 = Edge("B","E",6)
e5 = Edge("D","E",2)
e6 = Edge("D","F",5)
e7 = Edge("E","F",2)
A = Node("A",[e1,e2])
B = Node("B",[e4])
C = Node("C",[e3])
D = Node("D",[e5,e6])
E = Node("E",[e7])
F = Node("F",[])
nodeDict = {"A":A,"B":B,"C":C,"D":D,"E":E,"F":F}
gr = Graph(nodeDict)
inputer = "hi"
while inputer != "quit":
    input1 = input("What is the start point? type quit to exit")
    input2 = input("What is the end point? type quit to exit")
    if input1 == "quit" or input2 == "quit":
        inputer = "quit"
        break
    searchProb = SearchProblem(input1,input2,gr)
    print("longest path is ")
    pathToString(searchAlgorithms.AStarSearch(searchProb, searchAlgorithms.badHeuristic))
    # if pathToString(searchAlgorithms.uniformCostSearch(searchProb)) is None:
    #     print("No Path exists between the two points!")
    # else:
    #     print("shortest path is ")
    #     pathToString(searchAlgorithms.uniformCostSearch(searchProb))
