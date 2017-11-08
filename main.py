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

# e1 = Edge("A","C",1)
# e2 = Edge("A","B",2)
# e3 = Edge("C","D",3)
# e4 = Edge("B","E",6)
# e5 = Edge("D","E",2)
# e6 = Edge("D","F",5)
# e7 = Edge("E","F",2)

e1=Edge("B1","B2",1)
e2=Edge("B6","B7",1)
e3=Edge("B9","B10",2)
e4=Edge("B11","B12",2)
e5=Edge("B7","I1",2)
e6=Edge("B8","I1",1)
e7=Edge("B9","I1",1)
e8=Edge("B10","I1",2)
e9=Edge("I1","I2",1)
e10=Edge("I2","I3",1)
e11=Edge("B1","I4",1)
e12=Edge("B2","I4",1)
e13=Edge("I3","I4",1)
e14=Edge("B1","I5",1)
e15=Edge("B4","I5",1)
e16=Edge("B5","I5",1)
e17=Edge("I4","I5",1)
e18=Edge("B10","I6",1)
e19=Edge("B12","I7",1)
e20=Edge("I6","I7",1)
e21=Edge("B4","I8",1)
e22=Edge("B11","I8",1)
e23=Edge("I7","I8",1)
e24=Edge("B2","I9",1)
e25=Edge("B3","I9",1)
e26=Edge("B3","I10",1)
e27=Edge("B4","I10",1)
e28=Edge("B11","I10",1)
e29=Edge("I8","I10",1)
e30=Edge("B3","I11",1)
e31=Edge("I9","I11",1)
e32=Edge("I10","I11",1)
e33=Edge("B9","I12",1)
e34=Edge("I12","I13",1)
e35=Edge("B13","I14",1)
e36=Edge("I6","I14",1)
e37=Edge("I7","I14",1)
e38=Edge("B12","I15",1)
e39=Edge("I7","I15",1)
e40=Edge("I10","I16",1)
e41=Edge("I11","I16",1)
e42=Edge("B13","I17",1)
e43=Edge("I13","I17",1)
e44=Edge("I14","I17",1)
e45=Edge("I15","I17",1)
e46=Edge("B5","I18",1)
e47=Edge("B7","I18",3)
e48=Edge("I1","I18",2)
e49=Edge("I2","I18",2)
e50=Edge("B11","I19",1)
e51=Edge("I15","I19",1)
e52=Edge("I16","I19",1)
e53=Edge("B9","I20",1)
e54=Edge("I6","I20",4)
e55=Edge("I12","I20",1)
e56=Edge("I13","I20",1)
e57=Edge("I14","I20",4)
e58=Edge("B6","I21",1)
e59=Edge("I2","I21",1)
e60=Edge("I3","I22",1)
e61=Edge("I21","I22",1)
e62=Edge("B6","I23",1)
e63=Edge("B8","I23",1)
e64=Edge("I12","I24",1)
e65=Edge("I23","I24",2)


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
    if searchAlgorithms.uniformCostSearch(searchProb) == []:
        print("No Path exists between the two points!")
    else:
        print("shortest path is ")
        pathToString(searchAlgorithms.uniformCostSearch(searchProb))
        print("longest path is ")
        pathToString(searchAlgorithms.AStarSearch(searchProb, searchAlgorithms.badHeuristic))
