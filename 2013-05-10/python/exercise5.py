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

#HO DECISO DI NON SCALARE LE SUPERFICI AGGIUNTE (SPORTELLO,COFANO E VANO MOTORE) VISTO CHE IN UN MODELLO 3D 
#LE DIMENSIONI DEI PEZZI SAREBBERO QUESTE NONOSTANTE SEMBRINO NON COMBACIARE COL MODELLO 2.5D

#prof_lat

p0 = [[-4,0,0],[4,0,0]]
c0 = BEZIER(S1)(p0)
l0 = MAP(c0)(Dom1D)

p1 = [[-4,0,0],[-4.3,1.5,0],[-5.7,1.5,0],[-6,0,0]]
c1 = BEZIER(S1)(p1)
l1 = MAP(c1)(Dom1D)

p2 = [[-6,0,0],[-6.4,-0.1,0],[-8.1,0.5,0]]
c2 = BEZIER(S1)(p2)
l2 = MAP(c2)(Dom1D)

p3 = [[-8.1,0.5,0],[-7.8,0.5,0]]
c3= BEZIER(S1)(p3)
l3 = MAP(c3)(Dom1D)

p4 = [[-7.8,0.5,0],[-6.5,1.6,0],[-5.8,1.5,0],[-5,1.8,0]]
c4 = BEZIER(S1)(p4)
l4 = MAP(c4)(Dom1D)

p5 = [[-5,1.8,0],[-2.3,3,0]]
c5 = BEZIER(S1)(p5)
l5 = MAP(c5)(Dom1D)

p6 = [[-2.3,3,0],[-2,3.3,0],[1,3.2,0],[3,2.8,0]]
c6 = BEZIER(S1)(p6)
l6 = MAP(c6)(Dom1D)

p7 = [[3,2.8,0],[6,1.5,0]]
c7 = BEZIER(S1)(p7)
l7 = MAP(c7)(Dom1D)

p8 = [[6,1.5,0],[7.5,1.5,0]]
c8 = BEZIER(S1)(p8)
l8 = MAP(c8)(Dom1D)

p9 = [[7.5,1.5,0],[7.6,1.4,0]]
c9 = BEZIER(S1)(p9)
l9 = MAP(c9)(Dom1D)

p10 = [[7.6,1.4,0],[7.6,1,0]]
c10 = BEZIER(S1)(p10)
l10 = MAP(c10)(Dom1D)

p11 = [[7.6,1,0],[7.8,1,0]]
c11 = BEZIER(S1)(p11)
l11 = MAP(c11)(Dom1D)

p12 = [[7.8,1,0],[7.7,0.8,0]]
c12 = BEZIER(S1)(p12)
l12 = MAP(c12)(Dom1D)

p13 = [[7.7,0.8,0],[7.6,0.8,0]]
c13 = BEZIER(S1)(p13)
l13 = MAP(c13)(Dom1D)

p14 = [[7.6,0.8,0],[7,0.5,0]]
c14 = BEZIER(S1)(p14)
l14 = MAP(c14)(Dom1D)

p15 = [[7,0.5,0],[6.7,0.6,0],[6.5,-0.5,0],[6,0,0]]
c15 = BEZIER(S1)(p15)
l15 = MAP(c15)(Dom1D)

p16 = [[4,0,0],[4.3,1.5,0],[5.7,1.5,0],[6,0,0]]
c16 = BEZIER(S1)(p16)
l16 = MAP(c16)(Dom1D)

lp=STRUCT([l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16])
lateral_prof = T([2])(-1.65)(lp)

#prof_sup
p17 = [[0,0,0],[-4,0,0]]
c17 = BEZIER(S1)(p17)
l17 = MAP(c17)(Dom1D)

p18 = [[-4,0,0],[-4.5,0,-0.2],[-5.5,0,-0.2],[-6,0,0]]
c18 = BEZIER(S1)(p18)
l18 = MAP(c18)(Dom1D)

p19 = [[-6,0,0],[-8,0,0.5]]
c19 = BEZIER(S1)(p19)
l19 = MAP(c19)(Dom1D)

p20 = [[-8,0,0.5],[-8.02,0,0.6],[-8.04,0,0.7],[-8.05,0,1]]
c20 = BEZIER(S1)(p20)
l20 = MAP(c20)(Dom1D)

p21 = [[-8.05,0,1],[-8.1,0,2.5]]
c21 = BEZIER(S1)(p21)
l21 = MAP(c21)(Dom1D)

p22 = [[0,0,0],[4,0,-0.2]]
c22 = BEZIER(S1)(p22)
l22 = MAP(c22)(Dom1D)

p23 = [[4,0,-0.2],[4.5,0,-0.2],[5.5,0,-0.2],[6,0,0]]
c23 = BEZIER(S1)(p23)
l23 = MAP(c23)(Dom1D)

p24 = [[6,0,0],[8,0,0.5]]
c24 = BEZIER(S1)(p24)
l24 = MAP(c24)(Dom1D)

p25 = [[8,0,0.5],[8.02,0,0.6],[8.04,0,0.7],[8.05,0,1]]
c25 = BEZIER(S1)(p25)
l25 = MAP(c25)(Dom1D)

p26 = [[8.05,0,1],[8.1,0,2.5]]
c26 = BEZIER(S1)(p26)
l26 = MAP(c26)(Dom1D)




pr = STRUCT([l17,l18,l19,l20,l21,l22,l23,l24,l25,l26])

pr_ok = T([3])(-2.5)(pr)

pr1 = R([2,3])(PI)(pr_ok)



superior_prof = S([1])([0.93])(STRUCT([pr_ok,pr1]))

#

p27 = [[0,0,0],[0,0,-2.2]]
c27 = BEZIER(S1)(p27)
l27 = MAP(c27)(Dom1D)

p28 = [[0,0,-2.2],[0,1,-2.5]]
c28 = BEZIER(S1)(p28)
l28 = MAP(c28)(Dom1D)

p29 = [[0,1,-2.5],[0,1.8,-2.5]]
c29 = BEZIER(S1)(p29)
l29 = MAP(c29)(Dom1D)

p30 = [[0,1.8,-2.5],[0,1.8,-2.2],[0,2,-2.2],[0,2,-2]]
c30 = BEZIER(S1)(p30)
l30 = MAP(c30)(Dom1D)

p31 = [[0,2,-2],[0,3.3,-1.7]]
c31 = BEZIER(S1)(p31)
l31 = MAP(c31)(Dom1D)

p32 = [[0,3.3,-1.7],[0,3.3,0]]
c32 = BEZIER(S1)(p32)
l32 = MAP(c32)(Dom1D)

pr_s = STRUCT([l27,l28,l29,l30,l31,l32])

pr_sez = T([2])(-1.65)(pr_s)

pr_sez2 = R([1,3])(PI)(pr_sez)

sez_prof =STRUCT([pr_sez,pr_sez2])

profiles = (STRUCT([lateral_prof,superior_prof,sez_prof]))


#tire
p01 = [[0.05,0.4,0],[0.1,0.3,0],[0.15,0.2,0],[0.2,0.1,0]]
c1 = BEZIER(S1)(p01)

p02 = [[-0.05,0.4,0],[-0.1,0.3,0],[-0.15,0.2,0],[-0.2,0.1,0]]
c2 = BEZIER(S1)(p02)

p03 = [[0.05,0.4,-0.1],[0.1,0.3,-0.1],[0.15,0.2,-0.1],[0.2,0.1,-0.1]]
c3 = BEZIER(S1)(p03)

p04 = [[-0.05,0.4,-0.1],[-0.1,0.3,-0.1],[-0.15,0.2,-0.1],[-0.2,0.1,-0.1]]
c4 = BEZIER(S1)(p04)

s13 = BEZIER(S2)([c1,c3])
surf13 = MAP(s13)(Inverted_Dom2D)

s24 = BEZIER(S2)([c2,c4])
surf24 = MAP(s24)(Inverted_Dom2D)

s12 = BEZIER(S2)([c1,c2])
surf12 = MAP(s12)(Inverted_Dom2D)

s34 = BEZIER(S2)([c3,c4])
surf34 = MAP(s34)(Inverted_Dom2D)

s_tire = STRUCT([surf13,surf24,surf12,surf34])

s_tire_T1 = R([1,2])(2*PI/5)(s_tire)
s_tire_T2 = R([1,2])(2*PI/5)(s_tire_T1)
s_tire_T3 = R([1,2])(2*PI/5)(s_tire_T2)
s_tire_T4 = R([1,2])(2*PI/5)(s_tire_T3)

p05 = [[-0.2,0,0],[-0.2,0.23,0],[0.2,0.23,0],[0.2,0,0]]
c5 = BEZIER(S1)(p05)

p06 = [[-0.2,0,0],[-0.2,-0.23,0],[0.2,-0.23,0],[0.2,0,0]]
c6 = BEZIER(S1)(p06)

p07 = [[-0.2,0,-0.1],[-0.2,0.23,-0.1],[0.2,0.23,-0.1],[0.2,0,-0.1]]
c7 = BEZIER(S1)(p07)

p08 = [[-0.2,0,-0.1],[-0.2,-0.23,-0.1],[0.2,-0.23,-0.1],[0.2,0,-0.1]]
c8 = BEZIER(S1)(p08)


s57 = BEZIER(S2)([c5,c7])
surf57 = MAP(s57)(Dom2D)

s68 = BEZIER(S2)([c6,c8])
surf68 = MAP(s68)(Dom2D)

s56 = BEZIER(S2)([c5,c6])
surf56 = MAP(s56)(Dom2D)

s78 = BEZIER(S2)([c7,c8])
surf78 = MAP(s78)(Dom2D)



p09 = [[-0.4,0,0],[-0.4,0.45,0],[0.4,0.45,0],[0.4,0,0]]
c09 = BEZIER(S1)(p09)

p10 = [[-0.4,0,0],[-0.4,-0.45,0],[0.4,-0.45,0],[0.4,0,0]]
c10 = BEZIER(S1)(p10)

p11 = [[-0.4,0,-0.3],[-0.4,0.45,-0.3],[0.4,0.45,-0.3],[0.4,0,-0.3]]
c11 = BEZIER(S1)(p11)

p12 = [[-0.4,0,-0.3],[-0.4,-0.45,-0.3],[0.4,-0.45,-0.3],[0.4,0,-0.3]]
c12 = BEZIER(S1)(p12)


p13 = [[-0.42,0,0],[-0.42,0.47,0],[0.42,0.47,0],[0.42,0,0]]
c13 = BEZIER(S1)(p13)

p14 = [[-0.42,0,0],[-0.42,-0.47,0],[0.42,-0.47,0],[0.42,0,0]]
c14 = BEZIER(S1)(p14)

p15 = [[-0.42,0,-0.3],[-0.42,0.47,-0.3],[0.42,0.47,-0.3],[0.42,0,-0.3]]
c15 = BEZIER(S1)(p15)

p16 = [[-0.42,0,-0.3],[-0.42,-0.47,-0.3],[0.42,-0.47,-0.3],[0.42,0,-0.3]]
c16 = BEZIER(S1)(p16)

s913 = BEZIER(S2)([c09,c13])
surf913 = MAP(s913)(Dom2D)

s1014 = BEZIER(S2)([c10,c14])
surf1014 = MAP(s1014)(Inverted_Dom2D)

s1115 = BEZIER(S2)([c11,c15])
surf1115 = MAP(s1115)(Inverted_Dom2D)

s1216 = BEZIER(S2)([c12,c16])
surf1216 = MAP(s1216)(Dom2D)

s911 = BEZIER(S2)([c09,c11])
surf911 = MAP(s911)(Inverted_Dom2D)

s1012 = BEZIER(S2)([c10,c12])
surf1012 = MAP(s1012)(Dom2D)

tire = STRUCT([s_tire,s_tire_T1,s_tire_T2,s_tire_T3,s_tire_T4,surf57,
               surf68,surf56,surf78,surf911,surf1012,
               surf911,surf1012,surf913,surf1014,surf1115,surf1216])
#casing
p17 = [[-0.52,0,0],[-0.52,0.6,0],[0.52,0.6,0],[0.52,0,0]]
c17 = BEZIER(S1)(p17)

p18 = [[-0.52,0,0],[-0.52,-0.6,0],[0.52,-0.6,0],[0.52,0,0]]
c18 = BEZIER(S1)(p18)

p19 = [[-0.52,0,-0.3],[-0.52,0.6,-0.3],[0.52,0.6,-0.3],[0.52,0,-0.3]]
c19 = BEZIER(S1)(p19)

p20 = [[-0.52,0,-0.3],[-0.52,-0.6,-0.3],[0.52,-0.6,-0.3],[0.52,0,-0.3]]
c20 = BEZIER(S1)(p20)

s1719 = BEZIER(S2)([c17,c19])
surf1719 = MAP(s1719)(Dom2D)

s1820 = BEZIER(S2)([c18,c20])
surf1820 = MAP(s1820)(Dom2D)

s1317 = BEZIER(S2)([c13,c17])
surf1317 = MAP(s1317)(Dom2D)

s1418 = BEZIER(S2)([c14,c18])
surf1418 = MAP(s1418)(Dom2D)

s1519 = BEZIER(S2)([c15,c19])
surf1519 = MAP(s1519)(Dom2D)

s1620 = BEZIER(S2)([c16,c20])
surf1620 = MAP(s1620)(Dom2D)

casing = (COLOR([0,0,0])(STRUCT([surf1719,surf1820,surf1317,surf1418,surf1519,surf1620])))

wheel = (STRUCT([tire,casing]))

v1 = (R([1,3])(2*PI)(STRUCT([wheel])))
scaled_wheels = S([1,2])([1.4,1.4])(v1)


visual = T([2])(-1.4)(scaled_wheels)

wheel1 = T([1])(-4.6)(visual)
wheel2 = T([1])(4.6)(visual)
wheel1_2 = STRUCT([wheel1,wheel2])
traslated_wheels1_2 = T([3])(2.6)(wheel1_2)
rotated_wheels3_4 = R([2,3])(PI)(traslated_wheels1_2)
traslated_wheels3_4 = T([2])([-2.5])(rotated_wheels3_4)

wheels = STRUCT([traslated_wheels1_2,traslated_wheels3_4])

#steering wheel
p0 = [[-0.175,0.7,0],[-0.175,0.91,0],[0.175,0.91,0],[0.175,0.7,0]]
c0 = BEZIER(S1)(p0)

p1 = [[-0.175,0.7,0.49],[-0.175,0.91,0.665],[0.175,0.91,0.665],[0.175,0.7,0.49]]
c1 = BEZIER(S1)(p1)

p2 = [[-0.175,0,0.7],[-0.175,0,0.945],[0.175,0,0.945],[0.175,0,0.7]]
c2 = BEZIER(S1)(p2)

p3 = [[-0.175,0.35,0.7],[-0.175,0.42,0.945],[0.175,0.42,0.945],[0.175,0.35,0.7]]
c3 = BEZIER(S1)(p3)

p4 = [[0.175,0.7,0],[0.175,0.49,0],[-0.175,0.49,0],[-0.175,0.7,0]]
c4 = BEZIER(S1)(p4)

p5 = [[0.175,0.7,0.49],[0.175,0.49,0.315],[-0.175,0.49,0.315],[-0.175,0.7,0.49]]
c5 = BEZIER(S1)(p5)

p6 = [[0.175,0,0.7],[0.175,0,0.49],[-0.175,0,0.49],[-0.175,0,0.7]]
c6 = BEZIER(S1)(p6)

p7 = [[0.175,0.35,0.7],[0.175,0.28,0.455],[-0.175,0.28,0.455],[-0.175,0.35,0.7]]
c7 = BEZIER(S1)(p7)



s03 = BEZIER(S2)([c0,c1,c3,c2])
surf03 = MAP(s03)(Inverted_Dom2D)

s47 = BEZIER(S2)([c4,c5,c7,c6])
surf47 = MAP(s47)(Inverted_Dom2D)

surf0 = STRUCT([surf03,surf47])

vol1 = STRUCT([surf0,R([1,3])(PI)(surf0)])
vol2 = STRUCT([R([2,3])(PI)(vol1)])


p8 = [[0,0.7,0],[0,-0.7,0]]
c8 = BEZIER(S1)(p8)

p9 = [[0,0.7,-0.1],[0,-0.7,-0.1]]
c9 = BEZIER(S1)(p9)

p10 = [[-0.2,0.7,0],[-0.2,-0.7,0]]
c10 = BEZIER(S1)(p10)

p11 = [[-0.2,0.7,-0.1],[-0.2,-0.7,-0.1]]
c11 = BEZIER(S1)(p11)

p12 = [[0,-0.05,0],[0,-0.05,-0.7]]
c12 = BEZIER(S1)(p12)

p13 = [[0,0.05,0],[0,0.05,-0.7]]
c13 = BEZIER(S1)(p13)

p14 = [[-0.2,-0.05,0],[-0.2,-0.05,-0.7]]
c14 = BEZIER(S1)(p14)

p15 = [[-0.2,0.05,0],[-0.2,0.05,-0.7]]
c15 = BEZIER(S1)(p15)

s89 = BEZIER(S2)([c8,c9])
surf89 = MAP(s89)(Dom2D)

s1011 = BEZIER(S2)([c10,c11])
surf1011 = MAP(s1011)(Inverted_Dom2D)

s810 = BEZIER(S2)([c8,c10])
surf810 = MAP(s810)(Inverted_Dom2D)

s911 = BEZIER(S2)([c9,c11])
surf911 = MAP(s911)(Dom2D)

s1213 = BEZIER(S2)([c12,c13])
surf1213 = MAP(s1213)(Dom2D)

s1415 = BEZIER(S2)([c14,c15])
surf1415 = MAP(s1415)(Inverted_Dom2D)

s1214 = BEZIER(S2)([c12,c14])
surf1214 = MAP(s1214)(Inverted_Dom2D)

s1315 = BEZIER(S2)([c13,c15])
surf1315 = MAP(s1315)(Dom2D)

p16 = [[0,-0.3,0],[0,-0.3,-0.3],[0,0.3,-0.3],[0,0.3,0]]
c16 = BEZIER(S1)(p16)

p17 = [[-0.2,-0.3,0],[-0.2,-0.3,-0.3],[-0.2,0.3,-0.3],[-0.2,0.3,0]]
c17 = BEZIER(S1)(p17)

s1617 = BEZIER(S2)([c16,c17])
surf1617 = MAP(s1617)(Dom2D)

s168 = BEZIER(S2)([c16,c8])
surf168 = MAP(s168)(Dom2D)

s1710 = BEZIER(S2)([c17,c10])
surf1710 = MAP(s1710)(Dom2D)

s_wheel = COLOR([0,0,0])(STRUCT([vol1,vol2,surf89,surf1011,surf810,surf911,
                                        surf1213,surf1415,surf1214,surf1315,surf1617,
                                        surf168,surf1710]))

rotated_s_w = R([2,3])(-PI/2)(s_wheel)
scaled_s_w = S([2,3])([0.4,0.4])(rotated_s_w)
steering_wheel = T([3])(1.6)(scaled_s_w)

#door
p0 = [[-4,-1,0],[-4.2,-0.625,0],[-4.2,0.125,0],[-4,0.3,0]]
c0 = BEZIER(S1)(p0)

p1 = [[-0.5,-1,0],[-0.3,-0.625,0],[-0.3,0.125,0],[-0.5,0.3,0]]
c1 = BEZIER(S1)(p1)

s01 = BEZIER(S2)([c0,c1])
surf01 = COLOR(RED)(MAP(s01)(Inverted_Dom2D))

p2 = [[-4,0.3,0],[-0.5,0.3,0]]
c2 = BEZIER(S1)(p2)

p3 = [[-4,0.3,0],[-2.5,1.6,0],[-1,1.35,0],[-0.4,1.35,0]]
c3 = BEZIER(S1)(p3)

p4 = [[-0.4,1.35,0],[-0.5,0.3,0]]
c4 = BEZIER(S1)(p4)

p5 = [[-4,0.1,0],[-2.5,1.4,0],[-1,1.15,0],[-0.6,1.15,0]]
c5 = BEZIER(S1)(p5)

p6 = [[-0.6,1.15,0],[-0.7,0.1,0]]
c6 = BEZIER(S1)(p6)

s35 = BEZIER(S2)([c3,c5])
surf35 = COLOR(RED)(MAP(s35)(Inverted_Dom2D))

s46 = BEZIER(S2)([c4,c6])
surf46 = COLOR(RED)(MAP(s46)(Inverted_Dom2D))

s25 = BEZIER(S2)([c2,c5])
surf25 = COLOR([0,110,110,0.5])(MAP(s25)(Inverted_Dom2D))

door = STRUCT([surf01,surf25,surf35,surf46])
traslated_door = T([3])(2.5)(door)

#hood
p0 = [[3.5,0,1.8],[5.5,0,2]]
c0 = BEZIER(S1)(p0)


p1 = [[3.5,0,-1.8],[5.5,0,-2]]
c1 = BEZIER(S1)(p1)


s01 = BEZIER(S2)([c0,c1])
surf01 = COLOR(RED)(MAP(s01)(Dom2D))

p2 = [[5.5,0,2],[5.9,0,2.1]]
c2 = BEZIER(S1)(p2)


p3 = [[5.5,0,-2],[5.9,0,-2.1]]
c3 = BEZIER(S1)(p3)


s23 = BEZIER(S2)([c2,c3])
surf23 = COLOR(RED)(MAP(s23)(Dom2D))

p4 = [[5.9,0,2.1],[7.3,0,1.8]]
c4 = BEZIER(S1)(p4)


p5 = [[5.9,0,-2.1],[7.3,0,-1.8]]
c5 = BEZIER(S1)(p5)


s45 = BEZIER(S2)([c4,c5])
surf45 = COLOR(RED)(MAP(s45)(Dom2D))

hood = STRUCT([surf01,surf23,surf45])

traslated_hood = T([2])(0.27)(hood)

#engine compartment
p0 = [[-6,0,2.3],[-6.2,0,1.15],[-6.2,0,-1.15],[-6,0,-2.3]]
c0 = BEZIER(S1)(p0)


p1 = [[-3.5,0,2.2],[-3.8,0,2],[-3.8,0,-2],[-3.5,0,-2.2]]
c1 = BEZIER(S1)(p1)



s01 = BEZIER(S2)([c0,c1])
surf01 = COLOR(RED)(MAP(s01)(Inverted_Dom2D))

p2 = [[-6,0,2.3],[-7,0,1.9]]
c2 = BEZIER(S1)(p2)


p3 = [[-6,0,0.9],[-7,0,0.9]]
c3 = BEZIER(S1)(p3)


s23 = BEZIER(S2)([c2,c3])
surf23 = COLOR(YELLOW)(MAP(s23)(Inverted_Dom2D))

p4 = [[-6,0,-2.3],[-7,0,-1.9]]
c4 = BEZIER(S1)(p4)

p5 = [[-6,0,-0.9],[-7,0,-0.9]]
c5 = BEZIER(S1)(p5)

s45 = BEZIER(S2)([c4,c5])
surf45 = COLOR(YELLOW)(MAP(s45)(Dom2D))

p6 = [[-7,0,1.9],[-7,0,-1.9]]
c6 = BEZIER(S1)(p6)

p7 = [[-7.3,0,1.9],[-7.5,0,0.95],[-7.5,0,-1.15],[-7.3,0,-1.9]]
c7 = BEZIER(S1)(p7)

s67 = BEZIER(S2)([c6,c7])
surf67 = COLOR(RED)(MAP(s67)(Dom2D))

p8 = [[-7.1,0,0.9],[-7.1,0,-0.9]]
c8 = BEZIER(S1)(p8)

p9 = [[-5.5,0,0.9],[-5.5,0,-0.9]]
c9 = BEZIER(S1)(p9)

s89 = BEZIER(S2)([c8,c9])
surf89 = COLOR(RED)(MAP(s89)(Inverted_Dom2D))

engine_compartment = STRUCT([surf01,surf23,surf45,surf67,surf89])
traslated_engine_compartment = T([2])(0.27)(engine_compartment)


VIEW(STRUCT([profiles,wheels,steering_wheel,traslated_door,traslated_hood,traslated_engine_compartment]))
