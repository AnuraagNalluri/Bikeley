import util
import searchAlgorithms
import time
import requests
import json
import random
import datetime
import serial
import pdb
import ast

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

class SearchProblem:
    """
    This class outlines the structure of a search problem
    """
    def __init__(self, start, end, graph):
        self.startState = graph.nodes[start].name
        self.goalState = graph.nodes[end].name
        self.graph = graph

    def getStartState(self):
        return self.startState

    def isGoalState(self, state):
        return state==self.goalState

    def getSuccessors(self, state):
        successors=[]
        for edge in nodeDict2[state].getEdges():
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
    def __init__(self, start, end, weight, walkZone):
        self.start = start
        self.end = end
        self.weight = weight
        self.walkOnly = walkZone

class Graph:
    def __init__(self, nodeDict):
        self.nodes = nodeDict

def pathToString(path):
    for edge in path:
        print(edge.start + "  -->  " + edge.end)

def pathToList(path):
    pathList =[]
    pathList.append(coordDict[path[0].start])
    for edge in path:
        pathList.append(coordDict[edge.end])
    return pathList

e1=Edge("N2","N1",121,False)
e2=Edge("N1","N2",121,False)
e3=Edge("N2","N3",279,False)
e4=Edge("N5","N4",121,False)
e5=Edge("N1","N5",361,False)
e6=Edge("N58","N6",135,False)
e7=Edge("N49","N7",128,False)
e8=Edge("N9","N8",344,False)
e9=Edge("N8","N9",344,False)
e10=Edge("N4","N10",312,False)
e11=Edge("N10","N11",253,False)
e12=Edge("N11","N12",528,False)
e13=Edge("N49","N13",174,False)
e14=Edge("N54","N14",459,False)
e15=Edge("N55","N15",427,False)
e16=Edge("N17","N16",381,False)
e17=Edge("N1","N17",528,False)
e18=Edge("N61","N18",446,False)
e19=Edge("N21","N19",528,False)
e20=Edge("N21","N20",2112,False)
e21=Edge("N19","N21",1584,False)
e22=Edge("N67","N22",315,False)
e23=Edge("N16","N23",528,False)
e24=Edge("N16","N24",1056,False)
e25=Edge("N56","N25",528,False)
e26=Edge("N28","N26",449,False)
e27=Edge("N11","N27",446,False)
e28=Edge("N26","N28",449,False)
e29=Edge("N28","N29",404,False)
e30=Edge("N29","N30",472,False)
e31=Edge("N32","N31",1584,False)
e32=Edge("N31","N32",528,False)
e33=Edge("N31","N33",1584,False)
e34=Edge("N33","N34",1056,False)
e35=Edge("N36","N35",358,False)
e36=Edge("N35","N36",358,False)
e37=Edge("N35","N37",528,False)
e38=Edge("N35","N38",1056,False)
e39=Edge("N35","N39",1584,False)
e40=Edge("N74","N40",331,True)
e41=Edge("N42","N41",1056,False)
e42=Edge("N41","N42",1056,False)
e43=Edge("N44","N43",1056,False)
e44=Edge("N43","N44",1056,False)
e45=Edge("N72","N45",486,False)
e46=Edge("N76","N46",295,False)
e47=Edge("N71","N47",2112,False)
e48=Edge("N20","N48",528,False)
e49=Edge("N7","N49",128,False)
e50=Edge("N13","N50",151,False)
e51=Edge("N1","N51",213,False)
e52=Edge("N3","N52",226,False)
e53=Edge("N2","N53",282,False)
e54=Edge("N8","N54",164,False)
e55=Edge("N12","N55",1056,False)
e56=Edge("N25","N56",528,False)
e57=Edge("N10","N57",292,False)
e58=Edge("N6","N58",135,False)
e59=Edge("N6","N59",174,False)
e60=Edge("N16","N60",226,False)
e61=Edge("N18","N61",446,False)
e62=Edge("N19","N62",528,False)
e63=Edge("N16","N63",528,False)
e64=Edge("N18","N64",292,False)
e65=Edge("N23","N65",528,False)
e66=Edge("N19","N66",108,False)
e67=Edge("N22","N67",315,False)
e68=Edge("N21","N68",1584,False)
e69=Edge("N67","N69",1056,False)
e70=Edge("N44","N70",105,False)
e71=Edge("N44","N71",528,False)
e72=Edge("N44","N72",190,False)
e73=Edge("N43","N73",413,False)
e74=Edge("N40","N74",331,True)
e75=Edge("N24","N75",377,True)
e76=Edge("N23","N76",528,False)
e77=Edge("N46","N77",190,True)
e78=Edge("N25","N78",407,False)
e79=Edge("N26","N79",223,False)
e80=Edge("N28","N80",528,False)
e81=Edge("N35","N81",338,False)
e82=Edge("N35","N82",1056,False)
e83=Edge("N30","N83",200,False)
e84=Edge("N41","N84",272,False)
e85=Edge("N39","N85",528,False)
e86=Edge("N37","N86",276,False)
e87=Edge("N34","N87",528,False)
e88=Edge("N5","N1",361,False)
e89=Edge("N3","N2",279,False)
e90=Edge("N52","N3",226,False)
e91=Edge("N10","N4",312,False)
e92=Edge("N4","N5",121,False)
e93=Edge("N59","N6",174,False)
e94=Edge("N59","N7",213,False)
e95=Edge("N49","N8",276,False)
e96=Edge("N49","N9",144,False)
e97=Edge("N11","N10",528,False)
e98=Edge("N12","N11",305,False)
e99=Edge("N27","N12",325,False)
e100=Edge("N50","N13",151,False)
e101=Edge("N23","N16",1056,False)
e102=Edge("N16","N17",381,False)
e103=Edge("N63","N18",285,False)
e104=Edge("N62","N19",528,False)
e105=Edge("N48","N20",528,False)
e106=Edge("N20","N21",528,False)
e107=Edge("N24","N23",528,False)
e108=Edge("N23","N24",528,False)
e109=Edge("N75","N25",285,False)
e110=Edge("N57","N26",361,False)
e111=Edge("N28","N27",420,False)
e112=Edge("N27","N28",420,False)
e113=Edge("N30","N29",472,False)
e114=Edge("N83","N30",200,False)
e115=Edge("N33","N31",407,False)
e116=Edge("N33","N32",528,False)
e117=Edge("N32","N33",1584,False)
e118=Edge("N87","N34",528,False)
e119=Edge("N37","N35",528,False)
e120=Edge("N37","N36",486,False)
e121=Edge("N36","N37",486,False)
e122=Edge("N36","N38",1056,False)
e123=Edge("N37","N39",1056,False)
e124=Edge("N85","N40",184,True)
e125=Edge("N84","N41",272,False)
e126=Edge("N74","N42",397,False)
e127=Edge("N73","N43",413,False)
e128=Edge("N70","N44",105,False)
e129=Edge("N73","N45",495,False)
e130=Edge("N77","N46",190,True)
e131=Edge("N84","N47",233,False)
e132=Edge("N65","N48",495,False)
e133=Edge("N8","N49",276,False)
e134=Edge("N51","N50",213,False)
e135=Edge("N17","N51",528,False)
e136=Edge("N4","N52",1056,False)
e137=Edge("N3","N53",197,False)
e138=Edge("N14","N54",459,False)
e139=Edge("N15","N55",427,False)
e140=Edge("N52","N56",440,False)
e141=Edge("N11","N57",430,False)
e142=Edge("N50","N58",341,False)
e143=Edge("N7","N59",213,False)
e144=Edge("N17","N60",354,False)
e145=Edge("N23","N61",528,False)
e146=Edge("N21","N62",1056,False)
e147=Edge("N18","N63",528,False)
e148=Edge("N62","N64",331,False)
e149=Edge("N48","N65",495,False)
e150=Edge("N20","N66",174,False)
e151=Edge("N65","N67",312,False)
e152=Edge("N62","N68",2112,False)
e153=Edge("N68","N69",1056,False)
e154=Edge("N65","N70",528,False)
e155=Edge("N47","N71",2112,False)
e156=Edge("N45","N72",486,False)
e157=Edge("N44","N73",528,False)
e158=Edge("N42","N74",397,False)
e159=Edge("N25","N75",285,False)
e160=Edge("N24","N76",528,False)
e161=Edge("N74","N77",220,True)
e162=Edge("N56","N78",528,False)
e163=Edge("N28","N79",223,False)
e164=Edge("N79","N80",528,False)
e165=Edge("N36","N81",194,False)
e166=Edge("N37","N82",1056,False)
e167=Edge("N32","N83",144,False)
e168=Edge("N43","N84",253,False)
e169=Edge("N40","N85",184,True)
e170=Edge("N85","N86",2112,False)
e171=Edge("N35","N87",528,False)
e172=Edge("N17","N1",528,False)
e173=Edge("N53","N2",282,False)
e174=Edge("N53","N3",197,False)
e175=Edge("N52","N4",1056,False)
e176=Edge("N54","N8",164,False)
e177=Edge("N52","N10",1056,False)
e178=Edge("N27","N11",528,False)
e179=Edge("N55","N12",463,False)
e180=Edge("N24","N16",1056,False)
e181=Edge("N51","N17",528,False)
e182=Edge("N64","N18",292,False)
e183=Edge("N66","N19",108,False)
e184=Edge("N66","N20",174,False)
e185=Edge("N62","N21",2112,False)
e186=Edge("N60","N23",528,False)
e187=Edge("N53","N24",489,False)
e188=Edge("N78","N25",407,False)
e189=Edge("N79","N26",223,False)
e190=Edge("N55","N27",528,False)
e191=Edge("N29","N28",404,False)
e192=Edge("N55","N31",1056,False)
e193=Edge("N83","N32",144,False)
e194=Edge("N34","N33",528,False)
e195=Edge("N38","N35",1056,False)
e196=Edge("N38","N36",1056,False)
e197=Edge("N38","N37",528,False)
e198=Edge("N37","N38",528,False)
e199=Edge("N38","N39",1056,False)
e200=Edge("N85","N41",469,False)
e201=Edge("N85","N42",476,False)
e202=Edge("N74","N43",1056,False)
e203=Edge("N71","N44",528,False)
e204=Edge("N76","N45",243,False)
e205=Edge("N66","N48",528,False)
e206=Edge("N9","N49",144,False)
e207=Edge("N58","N50",341,False)
e208=Edge("N50","N51",213,False)
e209=Edge("N10","N52",1056,False)
e210=Edge("N16","N53",1056,False)
e211=Edge("N55","N54",528,False)
e212=Edge("N27","N55",528,False)
e213=Edge("N53","N56",463,False)
e214=Edge("N26","N57",361,False)
e215=Edge("N51","N58",528,False)
e216=Edge("N54","N59",528,False)
e217=Edge("N23","N60",528,False)
e218=Edge("N60","N61",190,False)
e219=Edge("N51","N62",1584,False)
e220=Edge("N23","N63",371,False)
e221=Edge("N66","N64",190,False)
e222=Edge("N63","N65",371,False)
e223=Edge("N48","N66",528,False)
e224=Edge("N68","N67",1584,False)
e225=Edge("N67","N68",528,False)
e226=Edge("N70","N69",1056,False)
e227=Edge("N67","N70",1056,False)
e228=Edge("N69","N71",217,False)
e229=Edge("N65","N72",528,False)
e230=Edge("N45","N73",495,False)
e231=Edge("N43","N74",1056,False)
e232=Edge("N76","N75",226,False)
e233=Edge("N45","N76",243,False)
e234=Edge("N75","N77",328,True)
e235=Edge("N77","N78",1056,True)
e236=Edge("N57","N79",482,False)
e237=Edge("N81","N80",148,False)
e238=Edge("N37","N81",466,False)
e239=Edge("N38","N82",476,False)
e240=Edge("N36","N83",325,False)
e241=Edge("N47","N84",233,False)
e242=Edge("N41","N85",2112,False)
e243=Edge("N87","N86",423,False)
e244=Edge("N83","N87",1056,False)
e245=Edge("N51","N1",213,False)
e246=Edge("N57","N10",292,False)
e247=Edge("N57","N11",1056,False)
e248=Edge("N53","N16",1056,False)
e249=Edge("N60","N17",354,False)
e250=Edge("N68","N21",2112,False)
e251=Edge("N61","N23",528,False)
e252=Edge("N60","N24",1056,False)
e253=Edge("N57","N27",427,False)
e254=Edge("N79","N28",223,False)
e255=Edge("N55","N33",2640,False)
e256=Edge("N39","N35",1584,False)
e257=Edge("N81","N36",194,False)
e258=Edge("N39","N37",1056,False)
e259=Edge("N39","N38",1056,False)
e260=Edge("N82","N39",469,False)
e261=Edge("N84","N43",253,False)
e262=Edge("N72","N44",190,False)
e263=Edge("N13","N49",174,False)
e264=Edge("N58","N51",528,False)
e265=Edge("N53","N52",423,False)
e266=Edge("N24","N53",489,False)
e267=Edge("N59","N54",528,False)
e268=Edge("N31","N55",1584,False)
e269=Edge("N57","N56",249,False)
e270=Edge("N27","N57",427,False)
e271=Edge("N24","N60",1056,False)
e272=Edge("N62","N61",528,False)
e273=Edge("N61","N62",528,False)
e274=Edge("N60","N63",528,False)
e275=Edge("N66","N65",1056,False)
e276=Edge("N63","N66",528,False)
e277=Edge("N69","N67",1584,False)
e278=Edge("N69","N68",1056,False)
e279=Edge("N71","N69",151,False)
e280=Edge("N69","N70",1584,False)
e281=Edge("N70","N72",295,False)
e282=Edge("N72","N73",528,False)
e283=Edge("N73","N74",528,False)
e284=Edge("N77","N75",328,True)
e285=Edge("N46","N76",528,False)
e286=Edge("N78","N77",1056,True)
e287=Edge("N79","N78",285,False)
e288=Edge("N78","N79",285,False)
e289=Edge("N82","N80",528,False)
e290=Edge("N38","N81",1056,False)
e291=Edge("N39","N82",469,False)
e292=Edge("N87","N83",1056,False)
e293=Edge("N42","N85",476,False)
e294=Edge("N86","N87",423,False)
e295=Edge("N60","N16",226,False)
e296=Edge("N63","N23",371,False)
e297=Edge("N75","N24",377,True)
e298=Edge("N80","N28",528,False)
e299=Edge("N81","N35",344,False)
e300=Edge("N83","N36",325,False)
e301=Edge("N81","N37",472,False)
e302=Edge("N81","N38",1056,False)
e303=Edge("N85","N39",528,False)
e304=Edge("N73","N44",528,False)
e305=Edge("N62","N51",1584,False)
e306=Edge("N56","N52",440,False)
e307=Edge("N52","N53",272,False)
e308=Edge("N33","N55",1584,False)
e309=Edge("N78","N56",528,False)
e310=Edge("N56","N57",308,False)
e311=Edge("N53","N60",1584,False)
e312=Edge("N63","N61",384,False)
e313=Edge("N64","N62",331,False)
e314=Edge("N61","N63",390,False)
e315=Edge("N67","N65",528,False)
e316=Edge("N64","N66",190,False)
e317=Edge("N70","N67",1056,False)
e318=Edge("N72","N70",295,False)
e319=Edge("N73","N72",528,False)
e320=Edge("N74","N73",528,False)
e321=Edge("N77","N74",220,True)
e322=Edge("N75","N76",226,False)
e323=Edge("N80","N79",528,False)
e324=Edge("N80","N81",148,False)
e325=Edge("N74","N82",528,False)
e326=Edge("N86","N85",1056,False)
e327=Edge("N63","N16",528,False)
e328=Edge("N65","N23",528,False)
e329=Edge("N76","N24",528,False)
e330=Edge("N82","N35",1056,False)
e331=Edge("N82","N37",1056,False)
e332=Edge("N82","N38",476,False)
e333=Edge("N56","N53",463,False)
e334=Edge("N54","N55",528,False)
e335=Edge("N79","N57",482,False)
e336=Edge("N61","N60",190,False)
e337=Edge("N68","N62",2112,False)
e338=Edge("N65","N63",371,False)
e339=Edge("N70","N65",528,False)
e340=Edge("N65","N66",528,False)
e341=Edge("N82","N74",528,False)
e342=Edge("N82","N79",528,False)
e343=Edge("N79","N82",528,False)
e344=Edge("N76","N23",528,False)
e345=Edge("N87","N35",364,False)
e346=Edge("N86","N37",276,False)
e347=Edge("N60","N53",1584,False)
e348=Edge("N63","N60",528,False)
e349=Edge("N66","N63",528,False)
e350=Edge("N72","N65",528,False)
e351=Edge("N80","N82",528,False)




N1 = Node("N1",[e2,e5,e17,e51],97.4533615112304)
N2 = Node("N2",[e1,e3,e53],97.5755615234375)
N3 = Node("N3",[e52,e89,e137],93.1951751708984)
N4 = Node("N4",[e10,e92,e136],101.704032897949)
N5 = Node("N5",[e4,e88],101.542427062988)
N6 = Node("N6",[e58,e59],108.274185180664)
N7 = Node("N7",[e49,e143],113.005531311035)
N8 = Node("N8",[e9,e54,e133],116.199890136718)
N9 = Node("N9",[e8,e206],107.509407043457)
N10 = Node("N10",[e11,e57,e91,e209],100.156547546386)
N11 = Node("N11",[e12,e27,e97,e141],102.500251770019)
N12 = Node("N12",[e55,e98],107.226409912109)
N13 = Node("N13",[e50,e263],107.96711730957)
N14 = Node("N14",[e138],136.167999267578)
N15 = Node("N15",[e139],127.932807922363)
N16 = Node("N16",[e23,e24,e60,e63,e102],84.8610382080078)
N17 = Node("N17",[e16,e135,e144,e172],85.477554321289)
N18 = Node("N18",[e61,e64,e147],82.3250350952148)
N19 = Node("N19",[e21,e62,e66],78.4778442382812)
N20 = Node("N20",[e48,e106,e150],75.7108688354492)
N21 = Node("N21",[e19,e20,e68,e146],72.1644592285156)
N22 = Node("N22",[e67],73.3698577880859)
N23 = Node("N23",[e65,e76,e101,e108,e145],73.6025390625)
N24 = Node("N24",[e75,e107,e160,e180,e266],83.5654830932617)
N25 = Node("N25",[e56,e78,e159],90.4944076538085)
N26 = Node("N26",[e28,e79,e214],98.4272994995117)
N27 = Node("N27",[e99,e112,e178,e212,e270],105.042381286621)
N28 = Node("N28",[e26,e29,e80,e111,e163],99.0079803466796)
N29 = Node("N29",[e30,e191],101.803794860839)
N30 = Node("N30",[e83,e113],104.628761291503)
N31 = Node("N31",[e32,e33,e268],118.018112182617)
N32 = Node("N32",[e31,e117,e167],108.75244140625)
N33 = Node("N33",[e34,e115,e116,e308],114.870864868164)
N34 = Node("N34",[e87,e194],107.709075927734)
N35 = Node("N35",[e36,e37,e38,e39,e81],97.3967514038085)
N36 = Node("N36",[e35,e121,e122,e165,e240],98.9051284790039)
N37 = Node("N37",[e86,e119,e120,e123,e166],92.5798873901367)
N38 = Node("N38",[e195,e196,e197,e199,e239],88.9287414550781)
N39 = Node("N39",[e85,e256,e258,e259,e291],86.7036743164062)
N40 = Node("N40",[e74,e169],82.9909591674804)
N41 = Node("N41",[e42,e84,e242],79.0518646240234)
N42 = Node("N42",[e41,e158,e293],79.7641677856445)
N43 = Node("N43",[e44,e73,e168,e231],76.3056411743164)
N44 = Node("N44",[e43,e70,e71,e72,e157],69.4931106567382)
N45 = Node("N45",[e156,e230,e233],74.7272262573242)
N46 = Node("N46",[e77,e285],82.7935180664062)
N47 = Node("N47",[e155,e241],72.9577026367187)
N48 = Node("N48",[e105,e149,e223],76.3727798461914)
N49 = Node("N49",[e7,e13,e95,e96],112.918029785156)
N50 = Node("N50",[e100,e142,e208],103.030220031738)
N51 = Node("N51",[e134,e181,e215,e219,e245],95.8717803955078)
N52 = Node("N52",[e90,e140,e175,e177,e307],94.1157531738281)
N53 = Node("N53",[e173,e174,e187,e213,e248],88.8072814941406)
N54 = Node("N54",[e14,e176,e216,e334],121.651405334472)
N55 = Node("N55",[e15,e179,e190,e192,e211],117.167922973632)
N56 = Node("N56",[e25,e162,e306,e310,e333],93.4432830810546)
N57 = Node("N57",[e110,e236,e246,e247,e253],97.0874633789062)
N58 = Node("N58",[e6,e207,e264],104.19822692871)
N59 = Node("N59",[e93,e94,e267],113.534492492675)
N60 = Node("N60",[e186,e218,e249,e252,e274],79.740608215332)
N61 = Node("N61",[e18,e251,e273,e314,e336],80.4153442382812)
N62 = Node("N62",[e104,e148,e152,e185,e272],86.9136962890625)
N63 = Node("N63",[e103,e222,e276,e296,e312],78.163215637207)
N64 = Node("N64",[e182,e313,e316],82.6931915283203)
N65 = Node("N65",[e132,e151,e154,e229,e328],71.9003753662109)
N66 = Node("N66",[e183,e184,e205,e221,e275],79.7001342773437)
N67 = Node("N67",[e22,e69,e225,e227,e315],70.061897277832)
N68 = Node("N68",[e153,e224,e250,e337],63.7263221740722)
N69 = Node("N69",[e228,e277,e278,e280],61.6040267944335)
N70 = Node("N70",[e128,e226,e281,e317,e339],67.5594863891601)
N71 = Node("N71",[e47,e203,e279],61.2296447753906)
N72 = Node("N72",[e45,e262,e282,e318,e350],69.5960235595703)
N73 = Node("N73",[e127,e129,e283,e304,e319],73.8585128784179)
N74 = Node("N74",[e40,e126,e161,e202,e320],82.8173904418945)
N75 = Node("N75",[e109,e234,e297,e322],83.8227462768554)
N76 = Node("N76",[e46,e204,e232,e329,e344],78.9299545288085)
N77 = Node("N77",[e130,e235,e284,e321],85.0258407592773)
N78 = Node("N78",[e188,e286,e288,e309],93.174331665039)
N79 = Node("N79",[e164,e189,e254,e287,e335],97.757080078125)
N80 = Node("N80",[e298,e323,e324,e351],98.3193893432617)
N81 = Node("N81",[e237,e257,e299,e301,e302],98.2296829223632)
N82 = Node("N82",[e260,e289,e330,e331,e332],89.5113296508789)
N83 = Node("N83",[e114,e193,e244,e300],105.354667663574)
N84 = Node("N84",[e125,e131,e261],75.9090270996093)
N85 = Node("N85",[e124,e170,e200,e201,e303],81.723533630371)
N86 = Node("N86",[e294,e326,e346],90.6234664916992)
N87 = Node("N87",[e118,e243,e292,e345],97.3377380371093)

nodeDict = {
					"Barker Hall": N21,
					"Koshland Hall": N20,
					"Li Ka Shing Center": N22,
					"Genetics and Plant Biology": N20,
					"Mulford Hall": N48,
					"Morgan Hall": N20,
					"Tolman Hall": N19,
					"Hilgard Hall": N18,
					"Wellman Hall": N18,
					"Gianini Hall": N18,
					"Life Sciences Addition": N23,
					"Valley Life Sciences Building (North)": N23,
					"Valley Life Sciences Building (South)": N45,
					"Moffitt Library": N24,
					"Haviland Hall": N16,
					"Starr East Asian Library": N3,
					"McCone Hal": N2,
					"North Gate Hall": N1,
					"O'Brien Hall": N4,
					"Hesse Hall": N4,
					"McLaughlin Hall (West Side)": N3,
					"McLaughlin Hall (East Side)": N4,
					"Blum Hall": N5,
					"Etcheverry Hall": N13,
					"Jacobs Hall": N6,
					"Soda Hall": N13,
					"Goldman School": N7,
					"Sutardja Dai Hall (West Side)": N5,
					"Sutardja Dai Hall (East Side)": N9,
					"Davis Hall": N4,
					"Bechtel Engineering Center": N4,
					"Evans Hall (Ground Floor)": N10,
					"Evans Hall (Floors 1 and Above)": N11,
					"Cory Hall": N9,
					"Hearst Memorial Mining Building": N11,
					"Stanley Hall": N12,
					"Foothill Residence Halls (North)": N14,
					"Foothill Residence Halls (South)": N15,
					"Pimental Hall": N27,
					"Latimer Hall": N27,
					"Tan Hall": N27,
					"Campbell Hall": N27,
					"Le Conte Hall": N26,
					"Birge Hall": N26,
					"Gilman Hall": N28,
					"Giauque Hall": N29,
					"Hildebrand Hall": N29,
					"Lewis Hall": N29,
					"Evans Diamond": N44,
					"Recreational Sports Facility": N47,
					"Haas Pavilion": N43,
					"Alumni House": N43,
					"Dwinelle Hall (West)": N45,
					"Dwinelle Hall (East)": N46,
					"Zellerbach Hall": N41,
					"Eshleman Hall": N41,
					"Cesar E. Chavez Student Center": N42,
					"Martin Luther King Jr. Student Union": N40,
					"Sproul Hall": N39,
					"Doe Memorial Library": N25,
					"California Hall": N24,
					"Hearst Field Annex": N38,
					"Barrows Hall": N39,
					"Wheeler Hall (North)": N25,
					"Wheeler Hall (South)": N46,
					"Campanile (Sather Tower)": N26,
					"Hearst Memorial Gymnasium": N37,
					"Kroeber Hall": N35,
					"Wurster Hall": N35,
					"Hertz Hall": N36,
					"Morrison Hall": N36,
					"Hangrove Music Library": N36,
					"Minor Hall": N30,
					"Haas School of Business (West)": N30,
					"Haas School of Business (East)": N31,
					"Calvin Laboratory": N32,
					"Boalt Hall": N34,
					"California Memorial Stadium": N33,
					"Maxwell Family Field and Stadium Garage": N31,
					"Upper Hearst Parking Structure": N8,
					"University House": N17
				}


# nodeDict = {"A":A,"B":B,"C":C,"D":D,"E":E,"F":F}
nodeDict2 = {
				"N1": N1,"N2": N2,"N3": N3,"N4": N4,"N5": N5,"N6": N6,
				"N7": N7,"N8": N8,"N9": N9,"N10": N10,"N11": N11,"N12": N12,
				"N13": N13,"N14": N14,"N15": N15,"N16": N16,"N17": N17,"N18": N18,
				"N19": N19,"N20": N20,"N21": N21,"N22": N22,"N23": N23,"N24": N24,
				"N25": N25,"N26": N26,"N27": N27,"N28": N28,"N29": N29,"N30": N30,
				"N31": N31,"N32": N32,"N33": N33,"N34": N34,"N35": N35,"N36": N36,
				"N37": N37,"N38": N38,"N39": N39,"N40": N40,"N41": N41,"N42": N42,
				"N43": N43,"N44": N44,"N45": N45,"N46": N46,"N47": N47,"N48": N48,
				"N49": N49,"N50": N50,"N51": N51,"N52": N52,"N53": N53,"N54": N54,
				"N55": N55,"N56": N56,"N57": N57,"N58": N58,"N59": N59,"N60": N60,
				"N61": N61,"N62": N62,"N63": N63,"N64": N64,"N65": N65,"N66": N66,
				"N67": N67,"N68": N68,"N69": N69,"N70": N70,"N71": N71,"N72": N72,
				"N73": N73,"N74": N74,"N75": N75,"N76": N76,"N77": N77,"N78": N78,
				"N79": N79,"N80": N80,"N81": N81,"N82": N82,"N83": N83,"N84": N84,
				"N85": N85,"N86": N86,"N87": N87
			}

coordDict = {
                "N1": (37.8745189,-122.2600489), "N2": (37.8741801,-122.2599954),
                "N3": (37.8737101,-122.259534), "N4": (37.8743601,-122.2588072),
                "N5": (37.8746691,-122.2589492), "N6": (37.8761915,-122.2590835),
                "N7": (37.8757003,-122.2583967), "N8": (37.875442,-122.2573721),
                "N9": (37.8750821,-122.258032), "N10": (37.873798,-122.2582807),
                "N11": (37.8738456,-122.2575224), "N12": (37.8738117,-122.2566533),
                "N13": (37.8752938,-122.2589171), "N14": (37.8753361,-122.2555912),
                "N15": (37.874701,-122.2549152), "N16": (37.8734137,-122.2609234),
                "N17": (37.8741674,-122.2613096), "N18": (37.8735576,-122.2626507),
                "N19": (37.8739472,-122.2639596), "N20": (37.8736296,-122.2644693),
                "N21": (37.8739642,-122.2652149), "N22": (37.8726599,-122.2649896),
                "N23": (37.8721518,-122.2620392), "N24": (37.8723635,-122.2603118),
                "N25": (37.8718003,-122.2589707), "N26": (37.8723296,-122.2574258),
                "N27": (37.873113,-122.2567981), "N28": (37.8721603,-122.2567391),
                "N29": (37.8724567,-122.255398), "N30": (37.8717453,-122.2545183),
                "N31": (37.8715928,-122.2530913), "N32": (37.8713133,-122.2539389),
                "N33": (37.8707967,-122.2525442), "N34": (37.8695856,-122.2527266),
                "N35": (37.8701276,-122.2549796), "N36": (37.8708475,-122.2553766),
                "N37": (37.8698481,-122.2562563), "N38": (37.8694416,-122.2575331),
                "N39": (37.869899,-122.2585523), "N40": (37.8692214,-122.2592819),
                "N41": (37.8686476,-122.2606471), "N42": (37.8694331,-122.259931),
                "N43": (37.8691155,-122.26161), "N44": (37.8706146,-122.2636914),
                "N45": (37.8712075,-122.2614759), "N46": (37.8709576,-122.2600275),
                "N47": (37.8683448,-122.2622591), "N48": (37.8726557,-122.2639757),
                "N49": (37.8753531,-122.2583324), "N50": (37.8752048,-122.2594213),
                "N51": (37.8750948,-122.2601509), "N52": (37.8736,-122.2587883),
                "N53": (37.8734984,-122.2596467), "N54": (37.8755224,-122.256825),
                "N55": (37.8738244,-122.255398), "N56": (37.8727658,-122.2586435),
                "N57": (37.8730834,-122.2579461), "N58": (37.8761364,-122.2595716),
                "N59": (37.8762931,-122.2585255), "N60": (37.8733078,-122.2612453),
                "N61": (37.8735831,-122.2618139), "N62": (37.8746628,-122.2631067),
                "N63": (37.8728251,-122.262404), "N64": (37.873799,-122.2632354),
                "N65": (37.8722958,-122.2634715), "N66": (37.873672,-122.2638631),
                "N67": (37.872012,-122.2643888), "N68": (37.8724736,-122.2659606),
                "N69": (37.8706188,-122.2657835), "N70": (37.8708645,-122.2639006),
                "N71": (37.8702123,-122.2657782), "N72": (37.8707755,-122.2630799),
                "N73": (37.8701784,-122.261712), "N74": (37.8701234,-122.2594643),
                "N75": (37.8715716,-122.2599256), "N76": (37.871398,-122.2606874),
                "N77": (37.8707162,-122.2596198), "N78": (37.8712625,-122.2580588),
                "N79": (37.8718511,-122.2574097), "N80": (37.8711016,-122.2561222),
                "N81": (37.8707586,-122.2558326), "N82": (37.8706654,-122.2576672),
                "N83": (37.8712117,-122.2544324), "N84": (37.8684422,-122.2614706),
                "N85": (37.8687302,-122.2592282), "N86": (37.8691198,-122.2560632),
                "N87": (37.8693061,-122.2546256)
}

gr = Graph(nodeDict)
# inputer = "hi"
# while inputer != "quit":
#     input1 = input("What is the start point? type quit to exit")
#     input2 = input("What is the end point? type quit to exit")
#     if input1 == "quit" or input2 == "quit":
#         inputer = "quit"
#         break

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

searchProb = SearchProblem(od['origin'],od['destination'],gr)
if searchAlgorithms.uniformCostSearch(searchProb) == []:
    print("No Path exists between the two points!")
elif sumz != 0:
    #print("shortest path is ")
    if od['time'] == '':
        X = pathToList(searchAlgorithms.BikeleySearch(searchProb,nodeDict2,None,searchAlgorithms.bikeleyHeuristic))
    else:
        X = pathToList(searchAlgorithms.BikeleySearch(searchProb,nodeDict2,int(od['time']),searchAlgorithms.bikeleyHeuristic))

else:
    if od['time'] == '':
        X = pathToList(searchAlgorithms.BikeleySearch(searchProb,nodeDict2,None,searchAlgorithms.trivialHeuristic))
    else:
        X = pathToList(searchAlgorithms.BikeleySearch(searchProb,nodeDict2,int(od['time']),searchAlgorithms.trivialHeuristic))
    # print("longest path is ")
    # pathToString(searchAlgorithms.AStarSearch(searchProb, searchAlgorithms.badHeuristic))
    # print("flatest path is ")
    # pathToString(searchAlgorithms.SteepSearch(searchProb,1,nodeDict2))
    # print("least flat path is ")
    # pathToString(searchAlgorithms.SteepSearch(searchProb,-1,nodeDict2))
    # print("least uphill path is ")
    # pathToString(searchAlgorithms.UphillSearch(searchProb,nodeDict2))
