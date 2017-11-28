import util
import searchAlgorithms

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

e1=Edge("N2","N1",121,True)
e2=Edge("N1","N2",121,True)
e3=Edge("N2","N3",279,True)
e4=Edge("N5","N4",121,True)
e5=Edge("N1","N5",361,True)
e6=Edge("N58","N6",135,True)
e7=Edge("N49","N7",128,True)
e8=Edge("N9","N8",344,True)
e9=Edge("N8","N9",344,True)
e10=Edge("N4","N10",312,True)
e11=Edge("N10","N11",253,True)
e12=Edge("N11","N12",528,True)
e13=Edge("N49","N13",174,True)
e14=Edge("N54","N14",459,True)
e15=Edge("N55","N15",427,True)
e16=Edge("N17","N16",381,True)
e17=Edge("N1","N17",528,True)
e18=Edge("N61","N18",446,True)
e19=Edge("N21","N19",528,True)
e20=Edge("N21","N20",2112,True)
e21=Edge("N19","N21",1584,True)
e22=Edge("N67","N22",315,True)
e23=Edge("N16","N23",528,True)
e24=Edge("N16","N24",1056,True)
e25=Edge("N56","N25",528,True)
e26=Edge("N28","N26",449,True)
e27=Edge("N11","N27",446,True)
e28=Edge("N26","N28",449,True)
e29=Edge("N28","N29",404,True)
e30=Edge("N29","N30",472,True)
e31=Edge("N32","N31",1584,True)
e32=Edge("N31","N32",528,True)
e33=Edge("N31","N33",1584,True)
e34=Edge("N33","N34",1056,True)
e35=Edge("N36","N35",358,True)
e36=Edge("N35","N36",358,True)
e37=Edge("N35","N37",528,True)
e38=Edge("N35","N38",1056,True)
e39=Edge("N35","N39",1584,True)
e40=Edge("N74","N40",331,False)
e41=Edge("N42","N41",1056,True)
e42=Edge("N41","N42",1056,True)
e43=Edge("N44","N43",1056,True)
e44=Edge("N43","N44",1056,True)
e45=Edge("N72","N45",486,True)
e46=Edge("N76","N46",295,True)
e47=Edge("N71","N47",2112,True)
e48=Edge("N20","N48",528,True)
e49=Edge("N7","N49",128,True)
e50=Edge("N13","N50",151,True)
e51=Edge("N1","N51",213,True)
e52=Edge("N3","N52",226,True)
e53=Edge("N2","N53",282,True)
e54=Edge("N8","N54",164,True)
e55=Edge("N12","N55",1056,True)
e56=Edge("N25","N56",528,True)
e57=Edge("N10","N57",292,True)
e58=Edge("N6","N58",135,True)
e59=Edge("N6","N59",174,True)
e60=Edge("N16","N60",226,True)
e61=Edge("N18","N61",446,True)
e62=Edge("N19","N62",528,True)
e63=Edge("N16","N63",528,True)
e64=Edge("N18","N64",292,True)
e65=Edge("N23","N65",528,True)
e66=Edge("N19","N66",108,True)
e67=Edge("N22","N67",315,True)
e68=Edge("N21","N68",1584,True)
e69=Edge("N67","N69",1056,True)
e70=Edge("N44","N70",105,True)
e71=Edge("N44","N71",528,True)
e72=Edge("N44","N72",190,True)
e73=Edge("N43","N73",413,True)
e74=Edge("N40","N74",331,False)
e75=Edge("N24","N75",377,False)
e76=Edge("N23","N76",528,True)
e77=Edge("N46","N77",190,False)
e78=Edge("N25","N78",407,True)
e79=Edge("N26","N79",223,True)
e80=Edge("N28","N80",528,True)
e81=Edge("N35","N81",338,True)
e82=Edge("N35","N82",1056,True)
e83=Edge("N30","N83",200,True)
e84=Edge("N41","N84",272,True)
e85=Edge("N39","N85",528,True)
e86=Edge("N37","N86",276,True)
e87=Edge("N34","N87",528,True)
e88=Edge("N5","N1",361,True)
e89=Edge("N3","N2",279,True)
e90=Edge("N52","N3",226,True)
e91=Edge("N10","N4",312,True)
e92=Edge("N4","N5",121,True)
e93=Edge("N59","N6",174,True)
e94=Edge("N59","N7",213,True)
e95=Edge("N49","N8",276,True)
e96=Edge("N49","N9",144,True)
e97=Edge("N11","N10",528,True)
e98=Edge("N12","N11",305,True)
e99=Edge("N27","N12",325,True)
e100=Edge("N50","N13",151,True)
e101=Edge("N23","N16",1056,True)
e102=Edge("N16","N17",381,True)
e103=Edge("N63","N18",285,True)
e104=Edge("N62","N19",528,True)
e105=Edge("N48","N20",528,True)
e106=Edge("N20","N21",528,True)
e107=Edge("N24","N23",528,True)
e108=Edge("N23","N24",528,True)
e109=Edge("N75","N25",285,True)
e110=Edge("N57","N26",361,True)
e111=Edge("N28","N27",420,True)
e112=Edge("N27","N28",420,True)
e113=Edge("N30","N29",472,True)
e114=Edge("N83","N30",200,True)
e115=Edge("N33","N31",407,True)
e116=Edge("N33","N32",528,True)
e117=Edge("N32","N33",1584,True)
e118=Edge("N87","N34",528,True)
e119=Edge("N37","N35",528,True)
e120=Edge("N37","N36",486,True)
e121=Edge("N36","N37",486,True)
e122=Edge("N36","N38",1056,True)
e123=Edge("N37","N39",1056,True)
e124=Edge("N85","N40",184,False)
e125=Edge("N84","N41",272,True)
e126=Edge("N74","N42",397,True)
e127=Edge("N73","N43",413,True)
e128=Edge("N70","N44",105,True)
e129=Edge("N73","N45",495,True)
e130=Edge("N77","N46",190,False)
e131=Edge("N84","N47",233,True)
e132=Edge("N65","N48",495,True)
e133=Edge("N8","N49",276,True)
e134=Edge("N51","N50",213,True)
e135=Edge("N17","N51",528,True)
e136=Edge("N4","N52",1056,True)
e137=Edge("N3","N53",197,True)
e138=Edge("N14","N54",459,True)
e139=Edge("N15","N55",427,True)
e140=Edge("N52","N56",440,True)
e141=Edge("N11","N57",430,True)
e142=Edge("N50","N58",341,True)
e143=Edge("N7","N59",213,True)
e144=Edge("N17","N60",354,True)
e145=Edge("N23","N61",528,True)
e146=Edge("N21","N62",1056,True)
e147=Edge("N18","N63",528,True)
e148=Edge("N62","N64",331,True)
e149=Edge("N48","N65",495,True)
e150=Edge("N20","N66",174,True)
e151=Edge("N65","N67",312,True)
e152=Edge("N62","N68",2112,True)
e153=Edge("N68","N69",1056,True)
e154=Edge("N65","N70",528,True)
e155=Edge("N47","N71",2112,True)
e156=Edge("N45","N72",486,True)
e157=Edge("N44","N73",528,True)
e158=Edge("N42","N74",397,True)
e159=Edge("N25","N75",285,True)
e160=Edge("N24","N76",528,True)
e161=Edge("N74","N77",220,False)
e162=Edge("N56","N78",528,True)
e163=Edge("N28","N79",223,True)
e164=Edge("N79","N80",528,True)
e165=Edge("N36","N81",194,True)
e166=Edge("N37","N82",1056,True)
e167=Edge("N32","N83",144,True)
e168=Edge("N43","N84",253,True)
e169=Edge("N40","N85",184,False)
e170=Edge("N85","N86",2112,True)
e171=Edge("N35","N87",528,True)
e172=Edge("N17","N1",528,True)
e173=Edge("N53","N2",282,True)
e174=Edge("N53","N3",197,True)
e175=Edge("N52","N4",1056,True)
e176=Edge("N54","N8",164,True)
e177=Edge("N52","N10",1056,True)
e178=Edge("N27","N11",528,True)
e179=Edge("N55","N12",463,True)
e180=Edge("N24","N16",1056,True)
e181=Edge("N51","N17",528,True)
e182=Edge("N64","N18",292,True)
e183=Edge("N66","N19",108,True)
e184=Edge("N66","N20",174,True)
e185=Edge("N62","N21",2112,True)
e186=Edge("N60","N23",528,True)
e187=Edge("N53","N24",489,True)
e188=Edge("N78","N25",407,True)
e189=Edge("N79","N26",223,True)
e190=Edge("N55","N27",528,True)
e191=Edge("N29","N28",404,True)
e192=Edge("N55","N31",1056,True)
e193=Edge("N83","N32",144,True)
e194=Edge("N34","N33",528,True)
e195=Edge("N38","N35",1056,True)
e196=Edge("N38","N36",1056,True)
e197=Edge("N38","N37",528,True)
e198=Edge("N37","N38",528,True)
e199=Edge("N38","N39",1056,True)
e200=Edge("N85","N41",469,True)
e201=Edge("N85","N42",476,True)
e202=Edge("N74","N43",1056,True)
e203=Edge("N71","N44",528,True)
e204=Edge("N76","N45",243,True)
e205=Edge("N66","N48",528,True)
e206=Edge("N9","N49",144,True)
e207=Edge("N58","N50",341,True)
e208=Edge("N50","N51",213,True)
e209=Edge("N10","N52",1056,True)
e210=Edge("N16","N53",1056,True)
e211=Edge("N55","N54",528,True)
e212=Edge("N27","N55",528,True)
e213=Edge("N53","N56",463,True)
e214=Edge("N26","N57",361,True)
e215=Edge("N51","N58",528,True)
e216=Edge("N54","N59",528,True)
e217=Edge("N23","N60",528,True)
e218=Edge("N60","N61",190,True)
e219=Edge("N51","N62",1584,True)
e220=Edge("N23","N63",371,True)
e221=Edge("N66","N64",190,True)
e222=Edge("N63","N65",371,True)
e223=Edge("N48","N66",528,True)
e224=Edge("N68","N67",1584,True)
e225=Edge("N67","N68",528,True)
e226=Edge("N70","N69",1056,True)
e227=Edge("N67","N70",1056,True)
e228=Edge("N69","N71",217,True)
e229=Edge("N65","N72",528,True)
e230=Edge("N45","N73",495,True)
e231=Edge("N43","N74",1056,True)
e232=Edge("N76","N75",226,True)
e233=Edge("N45","N76",243,True)
e234=Edge("N75","N77",328,False)
e235=Edge("N77","N78",1056,False)
e236=Edge("N57","N79",482,True)
e237=Edge("N81","N80",148,True)
e238=Edge("N37","N81",466,True)
e239=Edge("N38","N82",476,True)
e240=Edge("N36","N83",325,True)
e241=Edge("N47","N84",233,True)
e242=Edge("N41","N85",2112,True)
e243=Edge("N87","N86",423,True)
e244=Edge("N83","N87",1056,True)
e245=Edge("N51","N1",213,True)
e246=Edge("N57","N10",292,True)
e247=Edge("N57","N11",1056,True)
e248=Edge("N53","N16",1056,True)
e249=Edge("N60","N17",354,True)
e250=Edge("N68","N21",2112,True)
e251=Edge("N61","N23",528,True)
e252=Edge("N60","N24",1056,True)
e253=Edge("N57","N27",427,True)
e254=Edge("N79","N28",223,True)
e255=Edge("N55","N33",2640,True)
e256=Edge("N39","N35",1584,True)
e257=Edge("N81","N36",194,True)
e258=Edge("N39","N37",1056,True)
e259=Edge("N39","N38",1056,True)
e260=Edge("N82","N39",469,True)
e261=Edge("N84","N43",253,True)
e262=Edge("N72","N44",190,True)
e263=Edge("N13","N49",174,True)
e264=Edge("N58","N51",528,True)
e265=Edge("N53","N52",423,True)
e266=Edge("N24","N53",489,True)
e267=Edge("N59","N54",528,True)
e268=Edge("N31","N55",1584,True)
e269=Edge("N57","N56",249,True)
e270=Edge("N27","N57",427,True)
e271=Edge("N24","N60",1056,True)
e272=Edge("N62","N61",528,True)
e273=Edge("N61","N62",528,True)
e274=Edge("N60","N63",528,True)
e275=Edge("N66","N65",1056,True)
e276=Edge("N63","N66",528,True)
e277=Edge("N69","N67",1584,True)
e278=Edge("N69","N68",1056,True)
e279=Edge("N71","N69",151,True)
e280=Edge("N69","N70",1584,True)
e281=Edge("N70","N72",295,True)
e282=Edge("N72","N73",528,True)
e283=Edge("N73","N74",528,True)
e284=Edge("N77","N75",328,False)
e285=Edge("N46","N76",528,True)
e286=Edge("N78","N77",1056,False)
e287=Edge("N79","N78",285,True)
e288=Edge("N78","N79",285,True)
e289=Edge("N82","N80",528,True)
e290=Edge("N38","N81",1056,True)
e291=Edge("N39","N82",469,True)
e292=Edge("N87","N83",1056,True)
e293=Edge("N42","N85",476,True)
e294=Edge("N86","N87",423,True)
e295=Edge("N60","N16",226,True)
e296=Edge("N63","N23",371,True)
e297=Edge("N75","N24",377,False)
e298=Edge("N80","N28",528,True)
e299=Edge("N81","N35",344,True)
e300=Edge("N83","N36",325,True)
e301=Edge("N81","N37",472,True)
e302=Edge("N81","N38",1056,True)
e303=Edge("N85","N39",528,True)
e304=Edge("N73","N44",528,True)
e305=Edge("N62","N51",1584,True)
e306=Edge("N56","N52",440,True)
e307=Edge("N52","N53",272,True)
e308=Edge("N33","N55",1584,True)
e309=Edge("N78","N56",528,True)
e310=Edge("N56","N57",308,True)
e311=Edge("N53","N60",1584,True)
e312=Edge("N63","N61",384,True)
e313=Edge("N64","N62",331,True)
e314=Edge("N61","N63",390,True)
e315=Edge("N67","N65",528,True)
e316=Edge("N64","N66",190,True)
e317=Edge("N70","N67",1056,True)
e318=Edge("N72","N70",295,True)
e319=Edge("N73","N72",528,True)
e320=Edge("N74","N73",528,True)
e321=Edge("N77","N74",220,False)
e322=Edge("N75","N76",226,True)
e323=Edge("N80","N79",528,True)
e324=Edge("N80","N81",148,True)
e325=Edge("N74","N82",528,True)
e326=Edge("N86","N85",1056,True)
e327=Edge("N63","N16",528,True)
e328=Edge("N65","N23",528,True)
e329=Edge("N76","N24",528,True)
e330=Edge("N82","N35",1056,True)
e331=Edge("N82","N37",1056,True)
e332=Edge("N82","N38",476,True)
e333=Edge("N56","N53",463,True)
e334=Edge("N54","N55",528,True)
e335=Edge("N79","N57",482,True)
e336=Edge("N61","N60",190,True)
e337=Edge("N68","N62",2112,True)
e338=Edge("N65","N63",371,True)
e339=Edge("N70","N65",528,True)
e340=Edge("N65","N66",528,True)
e341=Edge("N82","N74",528,True)
e342=Edge("N82","N79",528,True)
e343=Edge("N79","N82",528,True)
e344=Edge("N76","N23",528,True)
e345=Edge("N87","N35",364,True)
e346=Edge("N86","N37",276,True)
e347=Edge("N60","N53",1584,True)
e348=Edge("N63","N60",528,True)
e349=Edge("N66","N63",528,True)
e350=Edge("N72","N65",528,True)
e351=Edge("N80","N82",528,True)



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
        print("flatest path is ")
        pathToString(searchAlgorithms.SteepSearch(searchProb,1,nodeDict2))
        print("least flat path is ")
        pathToString(searchAlgorithms.SteepSearch(searchProb,-1,nodeDict2))
        print("least uphill path is ")
        pathToString(searchAlgorithms.UphillSearch(searchProb,nodeDict2))
