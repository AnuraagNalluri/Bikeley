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

e1=Edge("B2","B1",121)
e2=Edge("B1","B2",121)
e3=Edge("I9","B3",95)
e4=Edge("I5","B4",200)
e5=Edge("I5","B5",56)
e6=Edge("B7","B6",315)
e7=Edge("B6","B7",315)
e8=Edge("I1","B8",125)
e9=Edge("B10","B9",364)
e10=Edge("B9","B10",364)
e11=Edge("B4","B11",384)
e12=Edge("B11","B12",1056)
e13=Edge("I14","B13",49)
e14=Edge("B7","I1",1056)
e15=Edge("B7","I2",161)
e16=Edge("I2","I3",213)
e17=Edge("B1","I4",36)
e18=Edge("B1","I5",361)
e19=Edge("B10","I6",167)
e20=Edge("B12","I7",36)
e21=Edge("B4","I8",299)
e22=Edge("B2","I9",180)
e23=Edge("B3","I10",226)
e24=Edge("B3","I11",194)
e25=Edge("B9","I12",144)
e26=Edge("I12","I13",528)
e27=Edge("B13","I14",49)
e28=Edge("B12","I15",194)
e29=Edge("I10","I16",440)
e30=Edge("B13","I17",108)
e31=Edge("B5","I18",125)
e32=Edge("B11","I19",203)
e33=Edge("B9","I20",259)
e34=Edge("B6","I21",135)
e35=Edge("I3","I22",338)
e36=Edge("B6","I23",161)
e37=Edge("I12","I24",348)
e38=Edge("I4","B1",36)
e39=Edge("I4","B2",164)
e40=Edge("I10","B3",226)
e41=Edge("I8","B4",299)
e42=Edge("I18","B5",125)
e43=Edge("I21","B6",135)
e44=Edge("I2","B7",161)
e45=Edge("I23","B8",217)
e46=Edge("I1","B9",295)
e47=Edge("I1","B10",144)
e48=Edge("I8","B11",85)
e49=Edge("I7","B12",36)
e50=Edge("I17","B13",125)
e51=Edge("B8","I1",125)
e52=Edge("I1","I2",325)
e53=Edge("I4","I3",171)
e54=Edge("B2","I4",157)
e55=Edge("B4","I5",200)
e56=Edge("I7","I6",312)
e57=Edge("I6","I7",312)
e58=Edge("B11","I8",85)
e59=Edge("B3","I9",95)
e60=Edge("B4","I10",1056)
e61=Edge("I9","I11",102)
e62=Edge("I13","I12",528)
e63=Edge("I17","I13",367)
e64=Edge("I6","I14",528)
e65=Edge("I7","I15",230)
e66=Edge("I11","I16",463)
e67=Edge("I13","I17",367)
e68=Edge("I15","I19",207)
e69=Edge("I6","I20",1584)
e70=Edge("I2","I21",341)
e71=Edge("I21","I22",223)
e72=Edge("B8","I23",217)
e73=Edge("I23","I24",436)
e74=Edge("I5","B1",361)
e75=Edge("I9","B2",180)
e76=Edge("I10","B4",1056)
e77=Edge("I23","B6",161)
e78=Edge("I18","B7",1584)
e79=Edge("I12","B9",144)
e80=Edge("I6","B10",167)
e81=Edge("I10","B11",528)
e82=Edge("I15","B12",194)
e83=Edge("B9","I1",295)
e84=Edge("I3","I2",213)
e85=Edge("I22","I3",338)
e86=Edge("I3","I4",171)
e87=Edge("B5","I5",56)
e88=Edge("I8","I7",240)
e89=Edge("I7","I8",528)
e90=Edge("I11","I9",102)
e91=Edge("B11","I10",528)
e92=Edge("I10","I11",272)
e93=Edge("I20","I12",374)
e94=Edge("I17","I14",174)
e95=Edge("I17","I15",233)
e96=Edge("I19","I16",249)
e97=Edge("I14","I17",174)
e98=Edge("I16","I19",308)
e99=Edge("I12","I20",374)
e100=Edge("I22","I21",223)
e101=Edge("I24","I23",436)
e102=Edge("I20","B9",259)
e103=Edge("I19","B11",203)
e104=Edge("B10","I1",144)
e105=Edge("I21","I2",341)
e106=Edge("I4","I5",328)
e107=Edge("I14","I7",217)
e108=Edge("I10","I8",1056)
e109=Edge("I8","I10",1056)
e110=Edge("I16","I11",463)
e111=Edge("I24","I12",348)
e112=Edge("I20","I14",1056)
e113=Edge("I19","I15",207)
e114=Edge("I15","I17",266)
e115=Edge("I13","I20",528)
e116=Edge("I2","I1",325)
e117=Edge("I15","I7",528)
e118=Edge("I16","I10",440)
e119=Edge("I14","I20",1584)
e120=Edge("I18","I1",272)



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
