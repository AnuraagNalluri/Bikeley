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
    def __init__(self, name, edges, elevation):
        self.name = name
        self.edges = edges
        self.elevation = elevation

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

e1=Edge("N2","N1",121)
e2=Edge("N1","N2",121)
e3=Edge("N2","N3",279)
e4=Edge("N5","N4",121)
e5=Edge("N1","N5",361)
e6=Edge("N13","N6",528)
e7=Edge("N13","N7",128)
e8=Edge("N13","N8",276)
e9=Edge("N13","N9",144)
e10=Edge("N4","N10",312)
e11=Edge("N10","N11",253)
e12=Edge("N11","N12",528)
e13=Edge("N6","N13",528)
e14=Edge("N6","N14",200)
e15=Edge("N1","N15",213)
e16=Edge("N9","N16",167)
e17=Edge("N3","N17",226)
e18=Edge("N2","N18",282)
e19=Edge("N8","N19",164)
e20=Edge("N12","N20",1056)
e21=Edge("N11","N21",217)
e22=Edge("N17","N22",440)
e23=Edge("N10","N23",292)
e24=Edge("N6","N24",135)
e25=Edge("N6","N25",164)
e26=Edge("N5","N1",361)
e27=Edge("N3","N2",279)
e28=Edge("N17","N3",226)
e29=Edge("N10","N4",312)
e30=Edge("N4","N5",121)
e31=Edge("N14","N6",200)
e32=Edge("N25","N7",213)
e33=Edge("N19","N8",164)
e34=Edge("N16","N9",167)
e35=Edge("N11","N10",528)
e36=Edge("N12","N11",305)
e37=Edge("N20","N12",463)
e38=Edge("N7","N13",128)
e39=Edge("N13","N14",325)
e40=Edge("N14","N15",213)
e41=Edge("N11","N16",322)
e42=Edge("N10","N17",1056)
e43=Edge("N3","N18",197)
e44=Edge("N20","N19",528)
e45=Edge("N19","N20",528)
e46=Edge("N12","N21",528)
e47=Edge("N18","N22",463)
e48=Edge("N21","N23",207)
e49=Edge("N14","N24",341)
e50=Edge("N7","N25",213)
e51=Edge("N15","N1",213)
e52=Edge("N18","N2",282)
e53=Edge("N18","N3",197)
e54=Edge("N24","N6",141)
e55=Edge("N17","N10",1056)
e56=Edge("N16","N11",322)
e57=Edge("N21","N12",364)
e58=Edge("N8","N13",276)
e59=Edge("N15","N14",213)
e60=Edge("N24","N15",528)
e61=Edge("N18","N17",423)
e62=Edge("N17","N18",272)
e63=Edge("N25","N19",528)
e64=Edge("N21","N20",528)
e65=Edge("N20","N21",528)
e66=Edge("N23","N22",249)
e67=Edge("N22","N23",308)
e68=Edge("N15","N24",528)
e69=Edge("N19","N25",528)
e70=Edge("N25","N6",164)
e71=Edge("N23","N10",292)
e72=Edge("N21","N11",217)
e73=Edge("N9","N13",144)
e74=Edge("N24","N14",341)
e75=Edge("N22","N17",440)
e76=Edge("N22","N18",463)
e77=Edge("N23","N21",207)
e78=Edge("N25","N24",308)
e79=Edge("N24","N25",308)
e80=Edge("N14","N13",325)



Node("N1",[e2,e5,e15],97.4533615112304)
Node("N2",[e1,e3,e18],97.5755615234375)
Node("N3",[e17,e27,e43],93.1951751708984)
Node("N4",[e10,e30],101.704032897949)
Node("N5",[e4,e26],101.542427062988)
Node("N6",[e13,e14,e24,e25],109.023330688476)
Node("N7",[e38,e50],113.005531311035)
Node("N8",[e19,e58],116.199890136718)
Node("N9",[e16,e73],107.509407043457)
Node("N10",[e11,e23,e29,e42],100.095268249511)
Node("N11",[e12,e21,e35,e41],102.500251770019)
Node("N12",[e20,e36,e46],107.226409912109)
Node("N13",[e6,e7,e8,e9,e39],112.918029785156)
Node("N14",[e31,e40,e49,e80],103.030220031738)
Node("N15",[e51,e59,e68],95.8717803955078)
Node("N16",[e34,e56],103.756690979003)
Node("N17",[e22,e28,e55,e62],94.1157531738281)
Node("N18",[e47,e52,e53,e61],88.8072814941406)
Node("N19",[e33,e45,e69],121.651405334472)
Node("N20",[e37,e44,e65],117.167922973632)
Node("N21",[e48,e57,e64,e72],101.961395263671)
Node("N22",[e67,e75,e76],93.4432830810546)
Node("N23",[e66,e71,e77],97.0874633789062)
Node("N24",[e54,e60,e74,e79],104.19822692871)
Node("N25",[e32,e63,e70,e78],113.534492492675)



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
