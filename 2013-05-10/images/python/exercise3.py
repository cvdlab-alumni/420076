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




Dom1D = INTERVALS(1)(40)
Dom2D= GRID([40,40])
Inverted_Dom2D = MAP([S2,S1])(GRID([40,40]))

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


VIEW(STRUCT([profiles,wheels]))
