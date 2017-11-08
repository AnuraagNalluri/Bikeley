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

e1=Edge("B1","B2",121 ft)
e2=Edge("B6","B7",315 ft)
e3=Edge("B9","B10",364 ft)
e4=Edge("B4","B11",384 ft)
e5=Edge("B11","B12",0.2 mi)
e6=Edge("B7","I1",0.2 mi)
e7=Edge("B8","I1",125 ft)
e8=Edge("B9","I1",295 ft)
e9=Edge("B10","I1",144 ft)
e10=Edge("I1","I2",325 ft)
e11=Edge("I2","I3",213 ft)
e12=Edge("B1","I4",36 ft)
e13=Edge("B2","I4",157 ft)
e14=Edge("I3","I4",171 ft)
e15=Edge("B4","I5",200 ft)
e16=Edge("B5","I5",56 ft)
e17=Edge("I4","I5",328 ft)
e18=Edge("B10","I6",167 ft)
e19=Edge("B12","I7",36 ft)
e20=Edge("I6","I7",312 ft)
e21=Edge("B4","I8",299 ft)
e22=Edge("B11","I8",85 ft)
e23=Edge("I7","I8",0.1 mi)
e24=Edge("B2","I9",180 ft)
e25=Edge("B3","I9",95 ft)
e26=Edge("B3","I10",226 ft)
e27=Edge("B4","I10",0.2 mi)
e28=Edge("B11","I10",0.1 mi)
e29=Edge("I8","I10",0.2 mi)
e30=Edge("B3","I11",194 ft)
e31=Edge("I9","I11",102 ft)
e32=Edge("I10","I11",272 ft)
e33=Edge("B9","I12",144 ft)
e34=Edge("I12","I13",0.1 mi)
e35=Edge("B13","I14",49 ft)
e36=Edge("I6","I14",0.1 mi)
e37=Edge("B12","I15",194 ft)
e38=Edge("I7","I15",230 ft)
e39=Edge("I10","I16",440 ft)
e40=Edge("I11","I16",463 ft)
e41=Edge("B13","I17",108 ft)
e42=Edge("I13","I17",367 ft)
e43=Edge("I14","I17",174 ft)
e44=Edge("I15","I17",266 ft)
e45=Edge("B5","I18",125 ft)
e46=Edge("B11","I19",203 ft)
e47=Edge("I15","I19",207 ft)
e48=Edge("I16","I19",308 ft)
e49=Edge("B9","I20",259 ft)
e50=Edge("I6","I20",0.3 mi)
e51=Edge("I12","I20",374 ft)
e52=Edge("I13","I20",0.1 mi)
e53=Edge("I14","I20",0.3 mi)
e54=Edge("B6","I21",135 ft)
e55=Edge("I2","I21",341 ft)
e56=Edge("I3","I22",338 ft)
e57=Edge("I21","I22",223 ft)
e58=Edge("B6","I23",161 ft)
e59=Edge("B8","I23",217 ft)
e60=Edge("I12","I24",348 ft)
e61=Edge("I23","I24",436 ft)


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
