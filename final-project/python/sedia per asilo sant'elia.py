from pyplasm import *
from pyplasm import *
import scipy
from scipy import *


def VERTEXTRUDE((V,coords)):
    return CAT(AA(COMP([AA(AR),DISTR]))(DISTL([V,coords])))

def larExtrude(model,pattern):
    V,FV = model
    d = len(FV[0])
    offset = len(V)
    m = len(pattern)
    outcells = []
    for cell in FV:
        # create the indices of vertices in the cell "tube"
        tube = [v + k*offset for k in range(m+1) for v in cell]
        # take groups of d+1 elements, via shifting by one
        rangelimit = len(tube)-d
        cellTube = [tube[k:k+d+1] for k in range(rangelimit)]
        outcells += [scipy.reshape(cellTube,newshape=(m,d,d+1)).tolist()]
    outcells = AA(CAT)(TRANS(outcells))
    outcells = [group for k,group in enumerate(outcells) if pattern[k]>0 ]
    coords = list(cumsum([0]+(AA(ABS)(pattern))))
    outVerts = VERTEXTRUDE((V,coords))
    newModel = outVerts, CAT(outcells)
    return newModel

def GRID(args):
    model = ([[]],[[0]])
    for k,steps in enumerate(args):
        model = larExtrude(model,steps*[1])
    V,cells = model
    verts = AA(list)(scipy.array(V) / AA(float)(args))
    return MKPOL([verts, AA(AA(lambda h:h+1))(cells), None])

#


Dom1D = INTERVALS(1)(10)
Dom2D= GRID([10,10])
Inverted_Dom2D = MAP([S2,S1])(GRID([10,10]))
D1 = INTERVALS(1)(40);
D2 = INTERVALS(PI/2)(40);
rot_domain = PROD([D1,D2]);

#BACK SUPPORT

p1 = [[2,0,2],[1.98,0,1.85],[1.78,0,1.85],[1.8,0,2]]
c1 = BEZIER(S1)(p1)
mapp1 = ROTATIONALSURFACE(c1)
s1 = MAP(mapp1)(rot_domain)


p2 = [[2,0,2],[1.98,0,2.15],[1.78,0,2.15],[1.8,0,2]]
c2 = BEZIER(S1)(p2)
mapp2 = ROTATIONALSURFACE(c2)
s2 = MAP(mapp2)(rot_domain)


sx_back_support = STRUCT([s1,s2])
dx_back_support = R([1,2])(PI/2)(sx_back_support)

#ARMRESTS

p3 = [[2,-1,2],[1.98,-1,1.85],[1.78,-1,1.85],[1.8,-1,2]]
c3 = BEZIER(S1)(p3)

p4 = [[2,-1,2],[1.98,-1,2.15],[1.78,-1,2.15],[1.8,-1,2]]
c4 = BEZIER(S1)(p4)

s13 = BEZIER(S2)([c1,c3])
surf13 = MAP(s13)(Dom2D)

s24 = BEZIER(S2)([c2,c4])
surf24 = MAP(s24)(Dom2D)

sx_armrest = STRUCT([surf13,surf24])
dx_arst = R([1,2])(PI)(sx_armrest)
dx_armrest = T([2])([-1])(dx_arst)

#SUPERIOR FRAME

superior_frame = STRUCT([sx_back_support,dx_back_support,sx_armrest,dx_armrest])

#FRONT TOP JUNCTIONS

p5 = [[2,-1.15,2],[2,-1,1.8],[1.8,-1,1.8],[1.8,-1.15,2]]
c5 = BEZIER(S1)(p5)

p6 = [[2,-1.15,2],[2,-1.3,2.1],[1.8,-1.3,2.1],[1.8,-1.15,2]]
c6 = BEZIER(S1)(p6)


p7 = [[2.02,-1.15,1.8],[2,-1,1.8],[1.8,-1,1.8],[1.78,-1.15,1.8]]
c7 = BEZIER(S1)(p7)

p8 = [[2.02,-1.15,1.8],[2,-1.3,1.8],[1.8,-1.3,1.8],[1.78,-1.15,1.8]]
c8 = BEZIER(S1)(p8)

s37 = BEZIER(S2)([c3,c5,c7])
surf37 = MAP(s37)(Dom2D)

s48 = BEZIER(S2)([c4,c6,c8])
surf48 = MAP(s48)(Dom2D)

front_top_sx_junction = STRUCT([surf37,surf48])
front_top_dx_junction = T([1])([-3.8])(front_top_sx_junction)

front_top_junctions = STRUCT([front_top_sx_junction,front_top_dx_junction])

#VERTICAL FRONT SUPPORTS

p9 = [[2.02,-1.15,-3.2],[2,-1,-3.2],[1.8,-1,-3.2],[1.78,-1.15,-3.2]]
c9 = BEZIER(S1)(p9)

p10 = [[2.02,-1.15,-3.2],[2,-1.3,-3.2],[1.8,-1.3,-3.2],[1.78,-1.15,-3.2]]
c10 = BEZIER(S1)(p10)

s79 = BEZIER(S2)([c7,c9])
surf79 = MAP(s79)(Dom2D)

s810 = BEZIER(S2)([c8,c10])
surf810 = MAP(s810)(Dom2D)

sx_front_vertical_support = STRUCT([surf79,surf810])
dx_front_vertical_support = T([1])([-3.8])(sx_front_vertical_support)
cfs = R([1,2])(-PI/2)(sx_armrest)
central_front_support1 = T([1,2,3])([-0.9,0.75,-2])(cfs)
central_front_support2 = T([1])([1])(central_front_support1)
central_front_support3 = T([1])([1])(central_front_support2)
central_front_support4 = T([1])([0.85])(central_front_support3)

central_front_support = T([3])([0.15])(STRUCT([central_front_support1,central_front_support2,central_front_support3,central_front_support4]))

front_vertical_supports = STRUCT([sx_front_vertical_support,dx_front_vertical_support,central_front_support])

#FRONT BOTTOM JUNCTIONS

fbsj = R([2,3])(PI/2)(front_top_sx_junction)
front_bottom_sx_junction = T([2,3])([0.85,-2.2])(fbsj)
front_bottom_dx_junction = T([1])([-3.8])(front_bottom_sx_junction)

front_bottom_junctions = STRUCT([front_bottom_sx_junction,front_bottom_dx_junction])

#FOOTS

sx_foot1 = T([3])([-5.35])(sx_armrest)
dx_foot1 = T([3])([-5.35])(dx_armrest)
sx_foot2 = T([2])([1])(sx_foot1)
dx_foot2 = T([2])([1])(dx_foot1)
sx_foot3 = T([2])([1])(sx_foot2)
dx_foot3 = T([2])([1])(dx_foot2)
sx_foot4 = T([2])([1])(sx_foot3)
dx_foot4 = T([2])([1])(dx_foot3)
foots = STRUCT([sx_foot1,dx_foot1,sx_foot2,dx_foot2,sx_foot3,dx_foot3,sx_foot4,dx_foot4])

#BACK BOTTOM JUNCTIONS

bbsj = R([2,3])(PI/2)(front_bottom_sx_junction)
back_bottom_sx_junction = T([2,3])([-0.25,-2.2])(bbsj)
back_bottom_dx_junction = T([1])([-3.8])(back_bottom_sx_junction)
back_bottom_junctions = STRUCT([back_bottom_sx_junction,back_bottom_dx_junction])

#BACK TOP JUNCTIONS
btsj = R([1,2])(-PI/2)(bbsj)
back_top_sx_junction_rotated = R([2,3])(PI)(btsj)
back_top_dx_junction_rotated = R([1,3])(PI)(btsj)
back_top_sx_junction = T([1,2,3])([-2.2,-0.24,-1.15])(back_top_sx_junction_rotated)
back_top_dx_junction = T([1,2,3])([2.2,3.55,-1.15])(back_top_dx_junction_rotated)

back_top_junctions = STRUCT([back_top_sx_junction,back_top_dx_junction])

#VERTICAL BACK SUPPORT

central_back_support_traslated = T([1,2])([-0.1,2.8])(STRUCT([central_front_support2,central_front_support3]))
central_back_support_rotated = R([2,3])(PI/8)(STRUCT([back_top_junctions,central_back_support_traslated]))

central_back_support = T([2,3])([0.15,-0.5])(central_back_support_rotated)

sbs = COLOR([0.8235,0.8235,0.8235])(CYLINDER([0.095,3.6])(60))
sbs_r = R([2,3])(PI/8)(sbs)
sbs_r2 = R([1,3])(PI/13)(sbs_r)
sx_back_support = T([1,2,3])([1.93,3.1,-3.22])(sbs_r2)
rbs_r = R([1,3])(-PI/13)(sbs_r)
rx_back_support = T([1,2,3])([-1.92,3.1,-3.2])(rbs_r)

vertical_back_support = STRUCT([central_back_support,sx_back_support,rx_back_support])

#SEANCE

seance1 = COLOR([0.588,0.294,0])(T([1,2,3])([-1.8,-1.2,0.1])(CUBOID([3.6,2,0.2])))

p11 = [[0,0,0],[0,1.3,0],[3.6,1.3,0],[3.6,0,0]]
c11 = BEZIER(S1)(p11)

p12 = [[0,0,0.2],[0,1.3,0.2],[3.6,1.3,0.2],[3.6,0,0.2]]
c12 = BEZIER(S1)(p12)

p13 = [[0,0,0],[0,0,0],[3.6,0,0],[3.6,0,0]]
c13 = BEZIER(S1)(p13)

p14 = [[0,0,0.2],[0,0,0.2],[3.6,0,0.2],[3.6,0,0.2]]
c14 = BEZIER(S1)(p14)

s1112 = BEZIER(S2)([c11,c12])
surf1112 = MAP(s1112)(Inverted_Dom2D)
s2 = COLOR([0.588,0.294,0])(surf1112)

s1113 = BEZIER(S2)([c11,c13])
surf1113 = MAP(s1113)(Inverted_Dom2D)
s3 = COLOR([0.588,0.294,0])(surf1113)

s1214 = BEZIER(S2)([c12,c14])
surf1214 = MAP(s1214)(Inverted_Dom2D)
s4 = COLOR([0.588,0.294,0])(surf1214)


seance2 = T([1,2,3])([-1.8,0.8,0.1])(STRUCT([s2,s3,s4]))

seance = T([3])([0.14])(STRUCT([seance1,seance2]))

#BACKREST

p15 = [[-0.1,0,0],[0,1,0],[1.5,1,0],[1.6,0,0]]
c15 = BEZIER(S1)(p15)

p16 = [[-0.2,0,0],[-0.2,1.2,0],[1.6,1.2,0],[1.7,0,0]]
c16 = BEZIER(S1)(p16)

p17 = [[-0.1,0,-1],[0,1,-1],[1.5,1,-1],[1.6,0,-1]]
c17 = BEZIER(S1)(p17)

p18 = [[-0.2,0,-1],[-0.2,1.2,-1],[1.6,1.2,-1],[1.7,0,-1]]
c18 = BEZIER(S1)(p18)

s1516 = BEZIER(S2)([c15,c16])
surf1516 = MAP(s1516)(Dom2D)

s1718 = BEZIER(S2)([c17,c18])
surf1718 = MAP(s1718)(Inverted_Dom2D)

s1517 = BEZIER(S2)([c15,c17])
surf1517 = MAP(s1517)(Inverted_Dom2D)

s1618 = BEZIER(S2)([c16,c18])
surf1618 = MAP(s1618)(Dom2D)

p19 = [[-0.1,0,0],[-0.2,0,0]]
c19 = BEZIER(S1)(p19)

p20 = [[-0.1,0,-1],[-0.2,0,-1]]
c20 = BEZIER(S1)(p20)

s1920 = BEZIER(S2)([c19,c20])
surf1920 = MAP(s1920)(Dom2D)

p21 = [[1.6,0,0],[1.7,0,0]]
c21 = BEZIER(S1)(p21)

p22 = [[1.6,0,-1],[1.7,0,-1]]
c22 = BEZIER(S1)(p22)

s2122 = BEZIER(S2)([c21,c22])
surf2122 = MAP(s2122)(Inverted_Dom2D)

backrest_s = S([1])([1.5])(STRUCT([surf1516,surf1718,surf1517,surf1618,surf1920,surf2122]))

backrest = COLOR([0.588,0.294,0])(T([1,2,3])([-1.1,0.9,2.5])(backrest_s))

VIEW(STRUCT([superior_frame,front_top_junctions,front_vertical_supports,front_bottom_junctions,
	foots,back_bottom_junctions,vertical_back_support,seance,backrest]))